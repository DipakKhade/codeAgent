from langchain_core.tools import tool
import os

@tool
def read_file(file_path:str) -> str:
    content = ''
    with open(file_path, 'r') as file:
        content = file.read()
    return content
    
