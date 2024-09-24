from sys import argv
from core.loader import load_tool
from typing import Callable

tool: Callable[[], str] = load_tool(name=argv[1])
result: str = tool()
print(result)