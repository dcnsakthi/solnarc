# Node.js Redis Application

## Prerequisites
1. Install [Node.js](https://nodejs.org/) (version 14 or higher recommended).
2. Ensure Redis is accessible at the specified host and port in the `.env` file.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd /workspaces/solnarc/redis/node
   ```
   
2. Initialize a New package.json:
   ```bash
    npm init -y
   ```

3. Install dependencies:
   ```bash
   npm install dotenv redis
   ```

4. Configure environment variables:
   - Create a `.env` file in the `/workspaces/solnarc/redis/node` directory.
   - Add the following variables (update values as needed):
     ```
     USERNAME=default
     PASSWORD=<your-redis-password>
     HOST=<your-redis-host>
     PORT=<your-redis-port>
     DB=<your-redis-database>
     ```

5. Run the application:
   ```bash
   node app.js
   ```

## Expected Output
The application will connect to Redis, set a key `owner` with the value `nsakthi`, and log `nsakthi` to the console.
