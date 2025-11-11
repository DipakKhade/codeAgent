from langchain_core.tools import tool
import subprocess
from typing import List

@tool
def exe_command(cmd: List[str]) -> None:
    """this function take command as the input, execute that command and return the result"""
    subprocess.run(cmd)
    return
