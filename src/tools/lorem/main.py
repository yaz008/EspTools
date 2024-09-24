from os import getenv
from sys import path
from core.filemanip import load_json
from core.tokenizer import Tokenizer
from tools.lorem.grammar import LoremGrammar
from tools.lorem.generate import generate_sentence, generate_lorem

def main() -> str:
    expr: str = getenv(key='ESPANSO_LOREM')
    tokenizer: Tokenizer = Tokenizer(rules=LoremGrammar)
    tokens: list[str] = tokenizer.tokenize(expr=expr)
    words: list[str] = load_json(path=f'{path[0]}\\tools\\lorem\\words.json')
    lorem: str = generate_lorem(tokens=tokens, words=words)
    if lorem == str():
        lorem = generate_sentence(length=5, words=words)
    return lorem