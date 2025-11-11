from langchain_core.tools import tool
import os

@tool
def delete_file(file_path: str) -> str:
    """this function will take the file path as input and delete that file and return the file path of deleted file"""
    os.remove(file_path)
    return file_path
