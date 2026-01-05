import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

print(f"API Key loaded: {api_key[:20]}..." if api_key else "API Key NOT found!")
print(f"Key length: {len(api_key) if api_key else 0}")