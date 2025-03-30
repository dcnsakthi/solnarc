import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from pymongo import ssl_support

# Load environment variables from .env file
load_dotenv()

# Ensure the URI is properly formatted without duplicate options
base_uri = os.getenv("MONGO_URI")
additional_options = "ssl=true&retryWrites=true&w=majority"
if "retryWrites=" in base_uri or "w=" in base_uri or "ssl=" in base_uri:
    uri = base_uri
else:
    uri = f"{base_uri}?{additional_options}" if "?" not in base_uri else f"{base_uri}&{additional_options}"

# Create a new client with SSL configuration
client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tls=True,  # Enable TLS/SSL
    tlsAllowInvalidCertificates=False  # Ensure certificates are valid
)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # list all databases
    databases = client.list_database_names()
    print("Databases:", databases)
    # list all collections in all the databases
    for db_name in databases:
        db = client[db_name]
        collections = db.list_collection_names()
        print(f"Collections in {db_name}:", collections)

# Close the connection
    client.close()
# Handle exceptions
except Exception as e:
    print(e)