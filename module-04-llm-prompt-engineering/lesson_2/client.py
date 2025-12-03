from dotenv import load_dotenv
import os
from openai import OpenAI


def get_client() -> OpenAI:
    """
    Load environment variables and return an OpenAI client.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Check your .env file.")

    client = OpenAI(api_key=api_key)
    return client
