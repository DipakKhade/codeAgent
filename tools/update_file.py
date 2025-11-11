from langchain_core.tools import tool

@tool
def update_file(file_path: str, content: str):
    with open(file_path, 'w+') as file:
        file.write(content)
    return