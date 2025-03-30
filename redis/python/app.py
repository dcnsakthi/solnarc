"""Basic connection example.
"""
import redis
from dotenv import load_dotenv
import os

load_dotenv()

r = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT')),
    decode_responses=True,
    username=os.getenv('REDIS_USERNAME'),
    password=os.getenv('REDIS_PASSWORD'),
)

success = r.set('county', 'Singapore')
# True

result = r.get('county')
print(result)
# >>> Singapore
