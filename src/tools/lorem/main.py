from os import getenv
from sys import path
from random import choices
from core.filemanip import load_json
from core.tokenizer import Tokenizer

def generate_sentence(length: int, words: list[str]) -> None:
    if length in (0, 1, 2):
        return ' '.join(['Lorem', 'ipsum'][:length])
    else:
        return ' '.join(['Lorem', 'ipsum'] + choices(words, k=length - 2))
    
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
    words: list[str] = load_json(path=f'{path[0]}\\tools\\lorem\\words.json')
    tokenizer: Tokenizer = Tokenizer(grammar=r'[\d]+|[\.]|[/]')
    tokens: list[str] = tokenizer.tokenize(expr=expr)
    return generate_lorem(tokens=tokens, words=words)