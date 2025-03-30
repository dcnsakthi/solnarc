# MSSQL .NET Console Application

This application connects to an MSSQL database, lists all schemas, and tables within each schema.

## Prerequisites

1. Install [.NET SDK](https://dotnet.microsoft.com/download) (version 6.0 or higher recommended).
2. Ensure MSSQL is accessible at the specified host and port.

## Setup Instructions

1. Navigate to the `/workspaces/solnarc/mssql/dotnet` directory.

2. Install dependencies:
   ```bash
   dotnet restore
   ```

3. Configure environment variables:
   - Create a `.env` file in the `/workspaces/solnarc/mssql/dotnet` directory.
   - Add the following variables:
     ```
     MSSQL_HOST=<your-mssql-host>
     MSSQL_PORT=<your-mssql-port>
     MSSQL_DATABASE=<your-database-name>
     MSSQL_USERNAME=<your-username>
     MSSQL_PASSWORD=<your-password>
     ```

4. Run the application:
   ```bash
   dotnet run
   ```

## Expected Output

The application will connect to MSSQL and display all schemas and their tables:
```
Connected to MSSQL!
Schemas and Tables:
Schema: dbo, Table: Users
Schema: dbo, Table: Orders
...
```
