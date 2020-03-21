
from dataclasses import dataclass


@dataclass
class BaseGraphics:
    type:  str   = ''
    width: float = 0.0

    def __str__(self):
        return f'BaseGraphics[type: {self.type}, width: {self.width}]'

    def __repr__(self):
        return self.__str__()
