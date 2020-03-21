
from dataclasses import dataclass


@dataclass
class BaseGraphics:
    """
    This class has the attributes shared between the `Node` and `Edge` classes
    """
    type:  str   = ''
    """
    The type of graphic
    """
    width: float = 0.0
    """
    The width of the line that draws the graphic
    """

    def __str__(self):
        return f'BaseGraphics[type: {self.type}, width: {self.width}]'

    def __repr__(self):
        return self.__str__()
