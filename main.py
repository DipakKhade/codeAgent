from langchain_google_genai import ChatGoogleGenerativeAI
from system_prompt.prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('GEMINI_API_KEY'))

llm = ChatGoogleGenerativeAI(
    model= "gemini-2.5-pro",
    temperature=1.0,
    max_retries=2,
    google_api_key= os.getenv('GEMINI_API_KEY'),
)

model = llm.bind_tools([])

res=model.invoke("What is 2+2?")

print(res)