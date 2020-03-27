
from typing import Tuple

from dataclasses import dataclass

from pygmlparser.graphics.Point import Point
from pygmlparser.graphics.BaseGraphics import BaseGraphics


@dataclass
class EdgeGraphics(BaseGraphics):

    arrow: str = ''
    """
    The type of arrow at the end of the line
    """
    line:  Tuple[Point] = ()
    """
    A list of `Points` that defines the `org.hasii.pygmlparser.Edge`.  This allows for drawing bends in the Edge.
    """

    def __str__(self) -> str:
        return f'EdgeGraphics[{self.__repr__()}] {super().__str__()}'
