from random import choices

def generate_sentence(length: int, words: list[str]) -> None:
    k: int = max(0, length - 2)
    words: list[str] = ['Lorem', 'ipsum'] + choices(words, k=k)
    return ' '.join(words[:length])
    
def generate_lorem(tokens: list[str], words: list[str]) -> str:
    lorem: str = str()
    for token in tokens:
        match token:
            case '.': lorem += '. '
            case '/': lorem += '\n'
            case number:
                lorem += generate_sentence(length=int(number),
                                           words=words)
    return lorem