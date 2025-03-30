using System;
using MongoDB.Driver;
using MongoDB.Bson;
using DotNetEnv;

Env.Load();
var connectionUri=Env.GetString("MONGO_URI");
if (string.IsNullOrEmpty(connectionUri)) {
    Console.WriteLine("Environment variable 'MONGO_URI' is not set.");
    return;
}

var settings = MongoClientSettings.FromConnectionString(connectionUri);

// Set the ServerApi field of the settings object to set the version of the Stable API on the client
settings.ServerApi = new ServerApi(ServerApiVersion.V1);

// Create a new client and connect to the server
var client = new MongoClient(settings);

// Send a ping to confirm a successful connection
try {
  var result = client.GetDatabase("admin").RunCommand<BsonDocument>(new BsonDocument("ping", 1));
  Console.WriteLine("Pinged your deployment. You successfully connected to MongoDB!");

  // List all databases
  var databaseNames = client.ListDatabaseNames().ToList();
  Console.WriteLine("Databases:");
  foreach (var dbName in databaseNames)
  {
      Console.WriteLine($"- {dbName}");

      // List all collections in the current database
      var db = client.GetDatabase(dbName);
      var collections = db.ListCollectionNames().ToList();
      Console.WriteLine($"  Collections in {dbName}:");
      foreach (var collection in collections)
      {
          Console.WriteLine($"  - {collection}");
      }
  }

  // Close the connection
  client.Cluster.Dispose();
} catch (Exception ex) {
  Console.WriteLine(ex);
}
