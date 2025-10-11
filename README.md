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

1. **AI Command Classification:** First, the user's prompt is sent to the Gemini API to classify the command type (DDL_DATABASE, DDL_TABLE, DML, or DQL). This determines the entire workflow.  
2. **Smart Connection Strategy:**
* If the command is DDL_DATABASE (e.g., "create a database"), the app intelligently connects to the MySQL server without a pre-selected database.
* For all other commands, a database name is required, and the app connects to it directly.
3. **Context-Aware Execution Path:**
* Database Commands: If the intent is to manage a database, the SQL is generated and executed immediately.
* CREATE TABLE Commands: A special, direct path is taken that bypasses table discovery, allowing the first table to be created in an empty database.
* All Other Table Commands (ALTER, DROP, SELECT, INSERT, etc.): The app follows the full discovery pipeline:

  1. Fetches a list of all existing tables.

  2. Asks the AI to identify the target table from the prompt.

  3. Fetches the specific schema for that table.

  4. Generates the final, context-aware SQL query.
4. **Execution & Display:** The generated query is executed, and the results (data, row count, or success message) are displayed to the user.

## **🛠️ Technology Stack**

* **Backend:** Python  
* **Frontend:** Streamlit  
* **Database:** MySQL (connected via mysql-connector-python)  
* **AI Model:** Google Gemini API (google-generativeai)  

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