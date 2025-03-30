import os
import pyodbc
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection details from .env
server = os.getenv("MSSQL_HOST")
database = os.getenv("MSSQL_DATABASE")
username = os.getenv("MSSQL_USERNAME")
password = os.getenv("MSSQL_PASSWORD")

def connect_to_db():
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )
        # print(f"Attempting to connect with connection string: {connection_string}")
        connection = pyodbc.connect(connection_string, timeout=5)
        print("Connection successful!")
        return connection
    except pyodbc.InterfaceError as e:
        print("ODBC Driver 17 for SQL Server not found or not configured properly.")
        print("Please ensure the driver is installed and accessible.")
        print(f"Error details: {e}")
        return None
    except pyodbc.OperationalError as e:
        print("Operational error occurred. Check server details and network connectivity.")
        print(f"Error details: {e}")
        return None
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def list_schemas_and_tables(connection):
    try:
        cursor = connection.cursor()
        # Query to list all schemas
        cursor.execute("SELECT name FROM sys.schemas")
        schemas = cursor.fetchall()
        print("Schemas:")
        for schema in schemas:
            print(f"- {schema[0]}")
            # Query to list tables in the current schema
            cursor.execute(f"""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_SCHEMA = '{schema[0]}'
            """)
            tables = cursor.fetchall()
            for table in tables:
                print(f"  - {table[0]}")
    except Exception as e:
        print(f"Error listing schemas and tables: {e}")

if __name__ == "__main__":
    connection = connect_to_db()
    if connection:
        list_schemas_and_tables(connection)
        connection.close()
