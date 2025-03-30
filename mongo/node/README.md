# MongoDB Node Application

## Prerequisites
1. Install [Node.js](https://nodejs.org/) (version 14 or higher recommended).
2. Ensure Mongo is accessible at the specified host and port in the `.env` file.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd /workspaces/solnarc/mongo/node
   ```
   
2. Initialize a New package.json:
   ```bash
    npm init -y
   ```

3. Install dependencies:
   ```bash
   npm install dotenv mongodb
   ```

4. Configure environment variables:
   - Create a `.env` file in the `/workspaces/solnarc/mongo/node` directory.
   - Add the following variables (update values as needed):
     ```
    MONGO_URI=mongodb+srv://<user>:<password>@<app>.si8rx.mongodb.net/?retryWrites=true&w=majority&appName=<app>

     ```

5. Run the application:
   ```bash
   node app.js
   ```

## Expected Output
The application will connect to Mongo, list the databases and collections, and log to the console.
