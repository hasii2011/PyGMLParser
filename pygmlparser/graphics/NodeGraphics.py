
from dataclasses import dataclass

from pygmlparser.graphics.BaseGraphics import BaseGraphics


@dataclass
class NodeGraphics(BaseGraphics):

    x: int = 0
    """
    x-coordinate
    """
    y: int = 0
    """
    y-coordinate
    """
    z: int = 0
    """
    z-coordinate for 3-D graphics
    """
    h: float = 0.0
    """
    height
    """
    w: float = 0.0
    """
    width
    """
    d: float = 0.0
    """
    depth for 3-D graphics
    """
    fill:    str = "#ff0000"
    """
    RGB value to fill graphic
    """
    outline: str = "#000000"
    """
    RGB value to outline the graphic
    """

    def __str__(self):
        meStr: str = (
            f'['
            f'NodeGraphics: x: {self.x:>4} y: {self.y:>4} z: {self.z:>2} '
            f'h:{self.h:>4} w: {self.w:>4} d: {self.d:>2} '
            f'fill: {self.fill} outline: {self.outline}'
            f']'
        )
        return f'{super().__str__()} {meStr}'

    def __repr__(self):
        return self.__str__()
