# MSSQL Node.js Application

This application connects to an MSSQL database, retrieves all schemas and tables, and displays them.

## Prerequisites

- Node.js installed
- MSSQL database credentials

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   npm install dotenv mssql
   ```

3. Create a `.env` file in the root directory with the following content:
   ```env
   MSSQL_HOST=<your-database-host>
   MSSQL_PORT=1433
   MSSQL_DATABASE=<your-database-name>
   MSSQL_USER=<your-username>
   MSSQL_PASSWORD=<your-password>
   ```

4. Run the application:
   ```bash
   node app.js
   ```

## Output

The application will list all schemas and tables in the database.
