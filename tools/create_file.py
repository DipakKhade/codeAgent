from langchain_core.tools import tool
import os

@tool
def create_file(file_name: str, file_path: str):
    with open(f"{file_name}//{file_path}", 'w') as file:
        pass
    return
    