from enum import StrEnum

class LoremGrammar(StrEnum):
    NUMBER: str = r'[\d]+'
    DOT: str = r'[\.]'
    SLASH: str = r'[/]'