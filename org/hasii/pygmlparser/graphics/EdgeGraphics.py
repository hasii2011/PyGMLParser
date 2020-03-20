
from typing import Tuple

from dataclasses import dataclass

from org.hasii.pygmlparser.graphics.Point import Point
from org.hasii.pygmlparser.graphics.BaseGraphics import BaseGraphics


@dataclass
class EdgeGraphics(BaseGraphics):

    arrow: str = ''
    line:  Tuple[Point] = ()
