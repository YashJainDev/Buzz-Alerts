from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

def get_gemini_response(prompt, model, temp=0.6):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temp,
            tools=[types.Tool(
                google_search=types.GoogleSearchRetrieval
            )]
        )
    )
    return response

def generate_notification_titles(prompt,model,temp=0.8):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temp,
        )
    )
    return response