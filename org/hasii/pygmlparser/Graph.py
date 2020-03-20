
class Graph:
    def __init__(self):
        self.graph_nodes = {}  # mapping id -> Node
        self.graph_edges = []  # set of Edge

    def __repr__(self):
        retStr: str = ''
        for nodeKey in self.graph_nodes.keys():
            retStr = f'{retStr} node: {nodeKey} - {self.graph_nodes[nodeKey]}'

        for edge in self.graph_edges:
            retStr = f'{retStr} --- {edge}'
        return retStr
