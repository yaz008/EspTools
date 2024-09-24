from importlib import import_module
from typing import Callable
from types import ModuleType

def load_tool(name: str) -> Callable[[], str]:
    tool: ModuleType = import_module(name=f'tools.{name}.main')
    return getattr(tool, 'main')