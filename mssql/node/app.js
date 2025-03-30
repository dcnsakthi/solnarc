require('dotenv').config();
const sql = require('mssql');

// Validate required environment variables
const requiredEnvVars = ['MSSQL_USER', 'MSSQL_PASSWORD', 'MSSQL_HOST', 'MSSQL_DATABASE'];
const missingEnvVars = requiredEnvVars.filter(envVar => !process.env[envVar]);

if (missingEnvVars.length > 0) {
    console.error(`Missing required environment variables: ${missingEnvVars.join(', ')}`);
    process.exit(1); // Exit the application if required variables are missing
}

const config = {
    user: process.env.MSSQL_USER,
    password: process.env.MSSQL_PASSWORD,
    server: process.env.MSSQL_HOST,
    database: process.env.MSSQL_DATABASE,
    options: {
        encrypt: true, // Use encryption
        trustServerCertificate: true // Change to false for production
    }
};

let pool;

async function initializePool() {
    try {
        pool = await new sql.ConnectionPool(config).connect();
        pool.on('error', err => {
            console.error('SQL Pool error', err);
        });
        console.log('Database connection pool initialized.');
    } catch (err) {
        console.error('Error creating pool:', err.message);
        if (err.code === 'ELOGIN') {
            console.error('Check your database login credentials.');
        }
        process.exit(1); // Exit if the pool cannot be initialized
    }
}

async function listSchemasAndTables() {
    if (!pool) {
        console.error('Pool is not initialized');
        return;
    }
    try {
        const request = pool.request();
        const result = await request.query(`
            SELECT 
                TABLE_SCHEMA, 
                TABLE_NAME 
            FROM INFORMATION_SCHEMA.TABLES 
            ORDER BY TABLE_SCHEMA, TABLE_NAME;
        `);
        console.dir(result.recordset);
        return result.recordset;
    } catch (err) {
        console.error('SQL error', err);
    }
}

// Initialize the pool and then list schemas and tables
(async () => {
    await initializePool();
    console.log('Listing all schemas and tables:');
    await listSchemasAndTables();
})();