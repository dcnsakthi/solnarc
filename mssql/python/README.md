# MSSQL Python Application

This Python script connects to a Microsoft SQL Server database, lists all schemas, and displays the tables within each schema.

## Prerequisites

1. **Python**: Ensure Python 3.6 or higher is installed.
2. **ODBC Driver**: Install the ODBC Driver 17 for SQL Server.
   - On Ubuntu/Debian:
     ```bash
     sudo su
     curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
     curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
     exit
     sudo apt-get update
     sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
     ```
   - On MacOS:
     ```bash
     brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
     brew update
     ACCEPT_EULA=Y brew install msodbcsql17
     ```
3. **Python Dependencies**: Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the same directory as the script and add the following variables:

```env
MSSQL_HOST=your_server_name_or_ip
MSSQL_DATABASE=your_database_name
MSSQL_USERNAME=your_username
MSSQL_PASSWORD=your_password
```

Replace `your_server_name_or_ip`, `your_database_name`, `your_username`, and `your_password` with your actual database credentials.

## How to Run

1. Ensure the `.env` file is properly configured.
2. Run the script:
   ```bash
   python app.py
   ```
3. The script will:
   - Attempt to connect to the database.
   - List all schemas in the database.
   - Display the tables within each schema.

## Troubleshooting

- **ODBC Driver Not Found**: Ensure the ODBC Driver 17 for SQL Server is installed and accessible.
- **Login Timeout**: Verify the server address, port (default is 1433), and network connectivity.
- **Operational Errors**: Check the database credentials and ensure the SQL Server allows remote connections.

## Example Output

```plaintext
Attempting to connect with connection string: DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server_name_or_ip;DATABASE=your_database_name;UID=your_username;PWD=your_password
Connection successful!
Schemas:
- dbo
  - Table1
  - Table2
- sales
  - Orders
  - Customers
```
