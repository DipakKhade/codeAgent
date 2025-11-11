from langchain_core.tools import tool
import os

@tool
def read_file(file_path:str) -> str:
    """this function will take file path as input and return the content of that file"""
    content = ''
    with open(file_path, 'r') as file:
        content = file.read()
    return content
    
