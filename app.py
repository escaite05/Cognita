import streamlit as st # type: ignore
import pandas as pd # type: ignore
from db_connector import create_connection, execute_query, get_table_schema, get_all_table_names
from gemini_handler import get_sql_from_gemini, identify_table_from_prompt, classify_command_type

st.set_page_config(page_title="Cognita", page_icon="🧠", layout="wide")
st.title("Cognita 🧠")
st.write("Query Made Human.")


st.sidebar.header("Database Connection")
db_name = st.sidebar.text_input("Database Name", placeholder="Enter name of the DB")

st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown('<center>Made with ❤️ by <a href="https://github.com/abhnva" style="text-decoration: none; color: inherit;"><b>abhnv</b></a></center>', unsafe_allow_html=True)

st.info(f"Connecting to database **`{db_name}`**. Your command will be classified before execution.")
user_question = st.text_area("Enter your command/question here:", height=150, placeholder="e.g. Show all students with marks above 90 OR create a new table...")

if st.button("🚀 Execute Command"):
    if not db_name or not user_question:
        st.warning("Please provide a database name and enter a command or question.")
    else:
        conn = create_connection(db_name)
        if not conn:
            st.error(f"Failed to connect to the database '{db_name}'.")
        else:
            with st.spinner("Classifying your command..."):
                command_type = classify_command_type(user_question)

            if command_type == "DDL":
                st.subheader("DDL Command Detected")
                with st.spinner("Generating DDL query..."):
                    sql_query = get_sql_from_gemini(user_question, "No schema context needed for DDL.")
                
                if sql_query:
                    st.info("Generated SQL Query:")
                    st.code(sql_query, language='sql')
                    results = execute_query(conn, sql_query)
                    if results is not None:
                        st.success("DDL command executed successfully!")
                    else:
                        st.error("An error occurred while executing the DDL command.")
                else:
                    st.error("Failed to generate DDL query.")
            
            elif command_type in ["DML", "DQL"]:
                st.subheader(f"{command_type} Command Detected")
                with st.spinner("Discovering tables..."):
                    available_tables = get_all_table_names(conn)
                
                if not available_tables:
                    st.error("Could not find any tables in the database.")
                else:
                    with st.expander("Discovered Tables"): st.write(available_tables)
                    
                    with st.spinner("Identifying table..."):
                        table_name = identify_table_from_prompt(user_question, available_tables)

                    if not table_name:
                        st.error("Could not identify a relevant existing table in your prompt.")
                    else:
                        st.success(f"Identified table: **`{table_name}`**")
                        schema = get_table_schema(conn, table_name)
                        
                        if schema:
                            with st.spinner("Generating SQL query..."):
                                sql_query = get_sql_from_gemini(user_question, schema)
                            
                            if not sql_query or "INCOMPLETE" in sql_query.upper():
                                st.warning("Request incomplete. For INSERT/UPDATE, please provide all necessary data.")
                            else:
                                st.info("Generated SQL Query:")
                                st.code(sql_query, language='sql')
                                results = execute_query(conn, sql_query)
                                if results is not None:
                                    if isinstance(results, list):
                                        if results: st.dataframe(pd.DataFrame(results))
                                        else: st.info("Query executed successfully but returned no data.")
                                    elif isinstance(results, int):
                                        st.success(f"Command executed successfully. {results} row(s) affected.")
                                else:
                                    st.error("An error occurred while executing the query.")
            else:
                st.error("Could not classify the command type. Please try rephrasing.")
            
            conn.close()