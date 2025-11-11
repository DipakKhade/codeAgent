from langchain_core.tools import tool
import os

@tool
def get_cwd()-> str:
    """this function will return the current working directory"""
    return os.getcwd()