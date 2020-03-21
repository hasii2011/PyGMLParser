
from dataclasses import dataclass


@dataclass
class Point:
    """
    Represents positions for GML graphics
    """
    x: int = 0
    """
    The x-coordinate
    """
    y: int = 0
    """
    The y-coordinate
    """
    z: int = 0
    """
    Valid for 3D graphics
    """
