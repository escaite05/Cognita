import mysql.connector
from mysql.connector import Error

def create_connection(db_name=None):
    try:
        connection_args = {
            'host': "localhost",
            'user': "root",
            'password': "root"
        }
        if db_name:
            connection_args['database'] = db_name

        conn = mysql.connector.connect(**connection_args)
        
        target = f"database '{db_name}'" if db_name else "MySQL server"
        print(f"Successfully connected to {target}")
        return conn
    except Error as e:
        print(f"DB Connection Error: {e}")
        return None

def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        # Check for DML commands
        if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
            connection.commit()
            print(f"Query committed. {cursor.rowcount} rows affected.")
            return cursor.rowcount
        else:
            # For SELECT
            result = cursor.fetchall()
            print("Query executed successfully, data fetched.")
            return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def get_table_schema(connection, table_name):
    # Fetch db schema and format
    try:
        query = f"DESCRIBE `{table_name}`;"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        columns = cursor.fetchall()
        
        formatted_schema = f"Table: `{table_name}`, Columns: "
        column_defs = [f"`{col['Field']}` ({col['Type']})" for col in columns]
        formatted_schema += ", ".join(column_defs)
        
        print(f"Successfully fetched schema for table: {table_name}")
        return formatted_schema
    except Error as e:
        print(f"Error fetching schema for table {table_name}: {e}")
        return None
    

def get_all_table_names(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        print(f"Found tables: {tables}")
        return tables
    except Error as e:
        print(f"Error fetching table names: {e}")
        return None