from os import getenv
from importlib import import_module
from typing import Any
from types import ModuleType

def main() -> str:
    expr: str = getenv(key='ESPANSO_EXPR')
    math: ModuleType = import_module(name='math')
    result: Any = eval(expr, math.__dict__)
    return str(result)