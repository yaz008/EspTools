from os import getenv
from sys import path
from random import choices
from core.filemanip import load_json
from core.tokenizer import Tokenizer
from tools.lorem.grammar import LoremGrammar

def generate_sentence(length: int, words: list[str]) -> None:
    k: int = max(0, length - 2)
    words: list[str] = ['Lorem', 'ipsum'] + choices(words, k=k)
    return ' '.join(words[:length])
    
def generate_lorem(tokens: list[str], words: list[str]) -> str:
    lorem: str = ''
    for token in tokens:
        match token:
            case '.':
                lorem += '. '
            case '/':
                lorem += '\n'
            case number:
                lorem += generate_sentence(length=int(number),
                                           words=words)
    return lorem

def main() -> str:
    expr: str = getenv(key='ESPANSO_LOREM')
    tokenizer: Tokenizer = Tokenizer(rules=LoremGrammar)
    tokens: list[str] = tokenizer.tokenize(expr=expr)
    words: list[str] = load_json(path=f'{path[0]}\\tools\\lorem\\words.json')
    return generate_lorem(tokens=tokens, words=words)