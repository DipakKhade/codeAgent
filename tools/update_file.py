from langchain_core.tools import tool

@tool
def update_file(file_path: str, content: str):
    """this function take file path and content as the input and write the content to the file"""
    with open(file_path, 'w+') as file:
        file.write(content)
    return