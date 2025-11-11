from langchain_google_genai import ChatGoogleGenerativeAI
from system_prompt.prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage

from tools.create_file import create_file
from tools.delete_file import delete_file
from tools.read_file import read_file
from tools.update_file import update_file

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=1.0,
    max_retries=2,
    google_api_key=os.getenv('GEMINI_API_KEY'),
)

tools = [create_file, delete_file, read_file, update_file]
model_with_tools = llm.bind_tools(tools)

messages = [
    SystemMessage(content=SYSTEM_PROMPT),
    HumanMessage(content="create a file index.html in the current directory and create a simple navbar in it")
]

response = model_with_tools.invoke(messages)
print(response)

if response.tool_calls:
    for tool_call in response.tool_calls:
        tool_name = tool_call['name']
        tool_args = tool_call['args']
        
        tool_map = {
            'create_file': create_file,
            'delete_file': delete_file,
            'read_file': read_file,
            'update_file': update_file
        }
        
        if tool_name in tool_map:
            result = tool_map[tool_name].invoke(tool_args)
            print(f"\nTool {tool_name} result:", result)