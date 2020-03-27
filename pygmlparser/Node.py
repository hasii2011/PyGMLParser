
from typing import cast

from pygmlparser.exceptions.GMLParseException import GMLParseException
from pygmlparser.graphics.NodeGraphics import NodeGraphics


class Node:
    """
    Represents a GML node
    """
    def __init__(self):

        self.id: int = cast(int, None)
        """
        The unique Node ID
        """
        self.is_anon = False
        """
        If `True` the node is anonymous
        """
        self.forward_edges  = []
        """
        edges where this node is the source
        """
        self.backward_edges = []
        """
        edges where this node is the target
        """
        self.graphics: NodeGraphics = NodeGraphics()
        """
        The Tulip <i>graphics</i> extension attributes
        """

    def validate(self, rawIdx: int):
        """
        Tests for the mandatory attribute id from GML

        Args:
            rawIdx: Index into the source input

        Raises
            `GMLParseException` if mandatory properties are not valid
        """

        if not isinstance(self.id, int):
            raise GMLParseException(f'[pos {rawIdx}] node has non-int id: {self.id}')

    def __str__(self):
        meStr: str = f'Node[id: {self.id} anonymous: {self.is_anon}] {self.graphics.__str__()}'
        return meStr

    def __repr__(self):
        return self.__str__()
