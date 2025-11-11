from langchain_core.tools import tool

@tool
def create_file(file_name: str, file_path: str) -> str :
    """this function take the file name and the file path as the input and create the file at the provided file path and return the path of created file"""
    print("calling me -------------------")
    with open(f"{file_path}/{file_name}", 'w') as file:
        pass
    return f"{file_name}/{file_path}"
