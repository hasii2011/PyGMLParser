
from typing import Tuple

from dataclasses import dataclass

from org.hasii.gmlparser.graphics.Point import Point
from org.hasii.gmlparser.graphics.BaseGraphics import BaseGraphics


@dataclass
class EdgeGraphics(BaseGraphics):

    arrow: str = ''
    line:  Tuple[Point] = ()
