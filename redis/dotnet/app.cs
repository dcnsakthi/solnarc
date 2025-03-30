using System; // Add this for Console
using StackExchange.Redis;
using DotNetEnv;

public class ConnectBasicExample
{
    public void run()
    {
        // Load environment variables from .env file
        Env.Load();

        var muxer = ConnectionMultiplexer.Connect(
            new ConfigurationOptions
            {
                EndPoints = { { Env.GetString("HOST"), Env.GetInt("PORT") } },
                User = Env.GetString("USERNAME"),
                Password = Env.GetString("PASSWORD")
            }
        );
        var db = muxer.GetDatabase();

        db.StringSet("name", "sakthi");
        RedisValue result = db.StringGet("name");
        Console.WriteLine(result); // >>> sakthi
    }

    public static void Main(string[] args) // Add this entry point
    {
        var example = new ConnectBasicExample();
        example.run();
    }
}
