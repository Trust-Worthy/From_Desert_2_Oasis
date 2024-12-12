from dotenv import load_dotenv
import os
from serpapi import GoogleSearch

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.environ.get("SERPAPI_KEY")

# Use the API key
print(api_key)


