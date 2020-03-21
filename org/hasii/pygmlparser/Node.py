
from typing import cast

from org.hasii.pygmlparser.exceptions.GMLParseException import GMLParseException

from org.hasii.pygmlparser.graphics.NodeGraphics import NodeGraphics


class Node:
    def __init__(self):
        # must have attribute id from GML
        self.graphics: NodeGraphics = NodeGraphics()

        self.id: int = cast(int, None)
        self.is_anon = False
        self.forward_edges  = []  # edges where this node is source
        self.backward_edges = []  # edges where this node is target

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
