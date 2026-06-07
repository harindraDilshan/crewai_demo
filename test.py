from dotenv import load_dotenv
import os
from google import genai


load_dotenv()
api_key = os.environ.get("GIMINI_API_KEY")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Expain AI withing one setence"
)



print(response.text)