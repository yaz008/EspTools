from re import findall
from dataclasses import dataclass, field
from enum import StrEnum

@dataclass(slots=True)
class Tokenizer:
    rules: StrEnum
    grammar: str = field(init=False)

    def __post_init__(self) -> None:
        self.grammar = '|'.join(self.rules)

    def tokenize(self, expr: str) -> list[str]:
        return findall(pattern=self.grammar, string=expr)