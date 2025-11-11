from langchain_core.tools import tool
import os

@tool
def delete_file(file_path: str):
    os.remove(file_path)
    return
