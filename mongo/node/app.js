import { MongoClient, ServerApiVersion } from 'mongodb';
import dotenv from 'dotenv';

dotenv.config();
// Connection URI
const uri = process.env.MONGO_URI;

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect the client to the server (optional starting in v4.7)
    await client.connect();

    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");

    // List all databases
    const databasesList = await client.db().admin().listDatabases();
    console.log("Databases:");
    for (const dbInfo of databasesList.databases) {
      console.log(`- ${dbInfo.name}`);

      // List all collections in the current database
      const db = client.db(dbInfo.name);
      const collections = await db.listCollections().toArray();
      console.log(`  Collections in ${dbInfo.name}:`);
      for (const collection of collections) {
        console.log(`  - ${collection.name}`);
      }
    }
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

run().catch(console.dir);
