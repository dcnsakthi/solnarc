using System;
using System.Data.SqlClient;
using DotNetEnv;

class Program
{
    static void Main(string[] args)
    {
        // Load environment variables from .env file
        Env.Load();

        string connectionString = $"Server={Env.GetString("MSSQL_HOST")},{Env.GetString("MSSQL_PORT")};" +
                                  $"Database={Env.GetString("MSSQL_DATABASE")};" +
                                  $"User Id={Env.GetString("MSSQL_USERNAME")};" +
                                  $"Password={Env.GetString("MSSQL_PASSWORD")};";

        try
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                Console.WriteLine("Connected to MSSQL!");

                string query = @"
                    SELECT s.name AS SchemaName, t.name AS TableName
                    FROM sys.schemas s
                    INNER JOIN sys.tables t ON t.schema_id = s.schema_id
                    ORDER BY s.name, t.name";

                using (SqlCommand command = new SqlCommand(query, connection))
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    Console.WriteLine("Schemas and Tables:");
                    while (reader.Read())
                    {
                        Console.WriteLine($"Schema: {reader["SchemaName"]}, Table: {reader["TableName"]}");
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
