import { createClient } from 'redis';
import dotenv from 'dotenv';

dotenv.config();

const client = createClient({
    username: process.env.USERNAME,
    password: process.env.PASSWORD,
    socket: {
        host: process.env.HOST,
        port: parseInt(process.env.PORT, 10) // Ensure PORT is parsed as an integer
    },
    database: parseInt(process.env.DB, 10) // Use the DB environment variable
});

client.on('error', err => console.log('Redis Client Error', err));

await client.connect();

await client.set('foo', 'bar');
const result = await client.get('foo');
console.log(result)  // >>> bar

