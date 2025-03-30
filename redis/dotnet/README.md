# .NET Redis Application

## Prerequisites
1. Install [.NET SDK](https://dotnet.microsoft.com/download) (version 6.0 or higher recommended).
2. Ensure Redis is accessible at the specified host and port in the `.env` file.

## Setup Instructions
1. Navigate to the `/workspaces/solnarc/redis/dotnet` directory.

2. Restore dependencies:
   ```bash
   dotnet restore
   ```

3. Configure environment variables:
   - Ensure the `.env` file is present in the `/workspaces/solnarc/redis/dotnet` directory.
   - Update the `.env` file with your Redis credentials:
     ```
     USERNAME=default
     PASSWORD=<your-redis-password>
     HOST=<your-redis-host>
     PORT=<your-redis-port>
     DB=<your-redis-database>
     ```

4. Run the application:
   ```bash
   dotnet run
   ```

## Expected Output
The application will connect to Redis, set a key `name` with the value `sakthi`, and log `sakthi` to the console.
