import json
from typing import Any

def load_json(path: str) -> Any:
    with open(file=path, mode='r', encoding='UTF-8') as json_file:
        return json.load(json_file)