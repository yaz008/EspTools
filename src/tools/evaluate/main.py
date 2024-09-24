from os import getenv
from importlib import import_module
from typing import Any
from types import ModuleType

def _main(expr: str) -> Any:
    math: ModuleType = import_module(name='math')
    return eval(expr, math.__dict__)

def main() -> str:
    expr: str = getenv(key='ESPANSO_EXPR')
    result: Any = _main(expr=expr)
    return str(result)