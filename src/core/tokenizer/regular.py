from re import findall
from dataclasses import dataclass

@dataclass(slots=True)
class Tokenizer:
    grammar: str

    def tokenize(self, expr: str) -> list[str]:
        return findall(pattern=self.grammar, string=expr)