from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")
print("API key loaded:", api_key is not None)

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Test call to the API
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Say hello to Frank and confirm that the API is working."
            }
        ],
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("API call failed:", e)
