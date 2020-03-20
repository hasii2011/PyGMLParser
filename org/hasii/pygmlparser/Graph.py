
from typing import cast
from typing import Dict
from typing import List
from typing import NewType

from org.hasii.pygmlparser.Edge import Edge
from org.hasii.pygmlparser.Node import Node


class Graph:

    Edges = NewType('Edges', List[Edge])
    Nodes = NewType('Nodes', Dict[int, Node])

    def __init__(self):
        self.graphNodes: Graph.Nodes = cast(Graph.Nodes, {})
        """
        Map of node IDs to Nodes
        """
        self.graphEdges: Graph.Edges = cast(Graph.Edges, [])
        """
        List of Edges
        """

    def __repr__(self):
        retStr: str = ''
        for nodeKey in self.graphNodes.keys():
            retStr = f'{retStr} node: {nodeKey} - {self.graphNodes[nodeKey]}'

        for edge in self.graphEdges:
            retStr = f'{retStr} --- {edge}'
        return retStr
