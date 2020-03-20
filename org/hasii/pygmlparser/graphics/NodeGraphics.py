
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
