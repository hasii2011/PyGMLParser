
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
        self.graph_nodes: Graph.Nodes = cast(Graph.Nodes, {})
        """
        Map of node IDs to Nodes
        """
        self.graph_edges: Graph.Edges = cast(Graph.Edges, [])
        """
        List of Edges
        """

    def __repr__(self):
        retStr: str = ''
        for nodeKey in self.graph_nodes.keys():
            retStr = f'{retStr} node: {nodeKey} - {self.graph_nodes[nodeKey]}'

        for edge in self.graph_edges:
            retStr = f'{retStr} --- {edge}'
        return retStr
