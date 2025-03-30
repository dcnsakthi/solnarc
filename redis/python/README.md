# Redis Python Example

## Setup

1. Install dependencies:
   ```bash
   pip install redis python-dotenv
   ```

2. Create a `.env` file in the same directory as `app.py` with the following content:
   ```dotenv
   REDIS_HOST=<your_redis_host>
   REDIS_PORT=<your_redis_port>
   REDIS_USERNAME=<your_redis_username>
   REDIS_PASSWORD=<your_redis_password>
   ```

3. Replace the placeholders with your actual Redis credentials.

## Run the Script

Execute the script using Python:
```bash
python app.py
```