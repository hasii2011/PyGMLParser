
from dataclasses import dataclass

from org.hasii.pygmlparser.graphics.BaseGraphics import BaseGraphics


@dataclass
class NodeGraphics(BaseGraphics):

    x: int = 0
    y: int = 0
    z: int = 0
    h: float = 0.0
    w: float = 0.0
    d: float = 0.0

    fill:    str = "#ff0000"
    outline: str = "#000000"

    def __str__(self):
        meStr: str = (
            f'['
            f'NodeGraphics: {self.x:>6} y: {self.y:>7} z: {self.z:>3} '
            f'h:{self.h:>4} w: {self.w:>4} d: {self.d:>2} '
            f'fill: {self.fill} outline: {self.outline}'
            f']'
        )
        return f'{super().__str__()} {meStr}'

    def __repr__(self):
        return self.__str__()
