# **Cognita 🧠**

**Query Made Human.** Cognita is an intelligent web application that translates natural language commands into executable MySQL queries. It serves as a powerful, user-friendly interface for interacting with databases, removing the need to write complex SQL code manually.

Built with Python, Streamlit, and the Google Gemini API, Cognita can understand and execute a wide range of database operations, from simple data retrieval to complex table modifications and definitions.

## **✨ Core Features**

* **Natural Language to SQL:** Ask questions or give commands in plain English. 
* **Full Spectrum SQL Support:**  
  * **DQL:** Fetches data using `SELECT`.  
  * **DML:** Manipulates data with `INSERT`, `UPDATE`, and `DELETE`.  
  * **DDL:** Manages database structure with `CREATE`, `ALTER`, and `DROP`.  
* **Intelligent Command Classification:** Automatically detects the user's intent (DDL vs. DML/DQL) to follow the correct execution path.  
* **Dynamic Schema Awareness:** Automatically discovers tables in the database and fetches the relevant table's structure to provide context to the AI, ensuring highly accurate queries.  
* **Interactive UI:** A clean and modern user interface built with Streamlit, featuring a Catppuccin-inspired theme.

## **🚀 How It Works: The Intelligent Pipeline**

Cognita doesn't just make a single, naive call to an AI. It follows a robust, multi-step process to ensure accuracy and safety, making it a truly intelligent assistant.

1. **AI Command Classification:** First, the user's prompt is sent to the Gemini API to classify the command type (DDL, DML, or DQL). This determines the entire workflow.  
2. **DDL Path (Structure Changes):**  
   * If the command is **DDL** (e.g., CREATE TABLE), the prompt is sent directly to the AI for SQL generation, as no existing table context is needed.  
3. **DML/DQL Path (Data Operations):**  
   * **Table Discovery:** The application connects to the database and fetches a list of all available tables.  
   * **AI Table Identification:** The user's prompt *and* the list of tables are sent to the AI, asking it to identify the most relevant table from the provided options. This dramatically improves accuracy.  
   * **Schema Fetching:** Once the table is identified, the application runs a DESCRIBE query to get its schema (column names and data types).  
   * **Final SQL Generation:** The user's prompt, along with the specific table schema, is sent to the AI to generate the final, context-aware, and highly accurate SQL query.  
4. **Execution & Display:** The generated query is executed against the database, and the results (data, row count, or success message) are displayed to the user.

## **🛠️ Technology Stack**

* **Backend:** Python  
* **Frontend:** Streamlit  
* **Database:** MySQL (connected via mysql-connector-python)  
* **AI Model:** Google Gemini API (google-generativeai)  
* **Secret Management:** python-dotenv

## **⚙️ Setup and Installation**

Follow these steps to get Cognita running on your local machine.

### **Prerequisites**

* Python 3.8+  
* MySQL Server installed and running.  
* A Google Gemini API Key.

### **Installation Steps**

1. **Clone the repository:**  
    ```
    git clone https://github.com/abhnva/cognita.git 
    cd cognita
    ```

2. **Create a virtual environment (recommended):**  
   ```
   python \-m venv venv  
   source venv/bin/activate  \# On Windows, use \`venv\\Scripts\\activate\`
   ```

3. **Install the required libraries:**  
   ```
   pip install \-r requirements.txt
   ```

4. **Set up your environment variables:**  
   Create a file named .env in the root of your project folder and add your credentials:  
   ```
   GOOGLE_API_KEY="your-google-gemini-api-key"
   ```  

5. **Run the application:**  
   ```
   streamlit run app.py
   ```

   The application should open in your default web browser.

## **Usage**

1. Enter the name of the database you wish to connect to in the sidebar.  
2. Type your command or question in the text area.  
3. Click "Execute Command".

### **Example Prompts**

* **DQL:** Show the names and wages of all workers from the worker table.  
* **DML:** Insert a new record into the students table with name 'Rohan' and marks 95 in class 11\.  
* **DDL:** Create a new table called 'projects' with an id (integer) and a project\_name (varchar).

## **👤 Author**

* **abhnv** \- [GitHub](https://github.com/abhnva)

## **📄 License**

This project is licensed under the MIT License.