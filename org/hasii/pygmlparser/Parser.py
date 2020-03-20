
from typing import List
from typing import NewType
from typing import Tuple
from typing import Union

from logging import Logger
from logging import getLogger

from org.hasii.pygmlparser.Edge import Edge
from org.hasii.pygmlparser.Graph import Graph
from org.hasii.pygmlparser.Node import Node
from org.hasii.pygmlparser.exceptions.GMLParseException import GMLParseException
from org.hasii.pygmlparser.graphics.Point import Point
from org.hasii.pygmlparser.graphics.EdgeGraphics import EdgeGraphics
from org.hasii.pygmlparser.graphics.NodeGraphics import NodeGraphics


class Parser:

    AttrObjectType = NewType('AttrObjectType', Union[Node, Edge, NodeGraphics, EdgeGraphics])
    LineType       = NewType('LineType', Tuple[Point, ...])

    GRAPHICS_TOKEN: str = 'graphics'
    START_TOKEN:    str = '['
    END_TOKEN:      str = ']'

    LINE_DEFINITION_TOKEN:  str = 'Line'
    POINT_DEFINITION_TOKEN: str = 'point'

    def __init__(self):
        self.logger: Logger = getLogger('Gml')
        # raw GML data (raw string split on whitespace)
        self._raw = []
        self._i = 0  # position (index) in self._raw

        self.graph = None

    def loadGML(self, path):
        with open(path) as infile:
            # NOTE: the split will destroy any spaces in string attributes
            self._raw = infile.read().strip().split()

        self._i:    int   = 0
        self.graph: Graph = Graph()

    def parse(self):
        if len(self._raw) == 0:
            raise GMLParseException('not loaded (must call load_gml before parse)')

        self._parseGraph()

    def _currentToken(self):
        if self._i >= len(self._raw):
            raise GMLParseException(f'[pos {self._i}] unexpected end of file')

        return self._raw[self._i]

    def _increment(self):
        self._i += 1

    def _parseGraph(self):
        self._parseOpenWithKeyword('graph')

        while self._currentToken() != ']':
            x = self._currentToken()
            self.logger.info(f'x: {x}')
            if x == 'node':
                self._parseNode()
            elif x == 'edge':
                self._parseEdge()
            else:
                self._parseAttribute(self.graph)
        self._increment()

    def _parseNode(self):
        self._parseOpenWithKeyword('node')

        node = Node()

        while self._currentToken() != ']':
            try:
                current: str = self._currentToken()
                if current == Parser.GRAPHICS_TOKEN:
                    self._parseNodeGraphics(node)
                else:
                    self._parseAttribute(node)
            except GMLParseException:
                self.logger.error(f'current: {self._currentToken()}')
                continue
        self.logger.info(f'Current index: {self._i}')
        self._increment()

        if not hasattr(node, 'id'):
            raise GMLParseException(f'[pos {self._i}] node has no id')

        nid = node.id

        if not isinstance(nid, int):
            raise GMLParseException(f'[pos {self._i}] node has non-int id: {nid}')

        if nid in self.graph.graph_nodes:
            raise GMLParseException(f'[pos {self._i}] redefinition of node id: {nid}')

        self.logger.info(f'Added Node: {node} with id: {nid}')
        self.graph.graph_nodes[nid] = node

    def _parseEdge(self):
        self._parseOpenWithKeyword('edge')

        edge: Edge = Edge()

        while self._currentToken() != ']':
            current: str = self._currentToken()
            if current == Parser.GRAPHICS_TOKEN:
                self._parseEdgeGraphics(edge)
            else:
                self._parseAttribute(edge)
        self._increment()

        if not hasattr(edge, 'source'):
            raise GMLParseException(f'[pos {self._i}] edge has no source')
        if not hasattr(edge, 'target'):
            raise GMLParseException(f'[pos {self._i}] edge has no target')

        if not isinstance(edge.source, int):
            raise GMLParseException(f'[pos {self._i}] edge has non-int source: {edge.source}')
        if not isinstance(edge.target, int):
            raise GMLParseException(f'[pos {self._i}] edge has non-int target: {edge.target}')

        for nid in (edge.source, edge.target):
            if nid not in self.graph.graph_nodes:
                node: Node = Node()
                node.is_anon = True
                node.id = nid
                self.graph.graph_nodes[nid] = node

        edge.source_node = self.graph.graph_nodes[edge.source]
        edge.target_node = self.graph.graph_nodes[edge.target]

        edge.source_node.forward_edges.append(edge)
        edge.target_node.backward_edges.append(edge)

        self.graph.graph_edges.append(edge)

    def _parseNodeGraphics(self, node: Node):

        self._parseOpenWithKeyword(Parser.GRAPHICS_TOKEN)
        graphics: NodeGraphics = NodeGraphics()

        while self._currentToken() != ']':
            self._parseAttribute(graphics)

        self._increment()
        self.logger.info(f'Current index: {self._i}')
        node.graphics = graphics

    def _parseEdgeGraphics(self, edge: Edge) -> Edge:

        self._parseOpenWithKeyword(Parser.GRAPHICS_TOKEN)
        graphics: EdgeGraphics = EdgeGraphics()
        while self._currentToken() != Parser.END_TOKEN:

            current: str = self._currentToken()
            if current == Parser.LINE_DEFINITION_TOKEN:
                graphics = self._parseLineDefinition(graphics)
            else:
                graphics = self._parseAttribute(graphics)

        self._increment()
        edge.graphics = graphics

        return edge

    def _parseLineDefinition(self, graphics: EdgeGraphics) -> EdgeGraphics:

        self._parseOpenWithKeyword(Parser.LINE_DEFINITION_TOKEN)

        #
        # We'll use a List because of the vagaries of Python data classes
        #
        lineList: List[Point] = []
        while self._currentToken() != Parser.END_TOKEN:
            current: str = self._currentToken()
            self.logger.info(f'current: {current}')

            lineList = self._parsePointDefinition(lineList)

        # But the data classes save a line definition as a Tuple of points
        graphics.line = tuple(lineList)

        self._increment()
        return graphics

    def _parsePointDefinition(self, lineList: List[Point]) -> List[Point]:

        self._parseOpenWithKeyword(Parser.POINT_DEFINITION_TOKEN)

        point: Point = Point()
        while self._currentToken() != Parser.END_TOKEN:
            self.logger.info(f'current: {self._currentToken()}')
            point = self._parseAttribute(point)

        lineList.append(point)

        self._increment()
        return lineList

    def _parseAttribute(self, obj: AttrObjectType) -> AttrObjectType:
        """

        Args:
            obj: The object we update attributes on


        Returns:
            The update object
        """
        name = self._currentToken()
        if not name.isalnum():
            raise GMLParseException(f'[pos {self._i}] attribute name is not alphanumeric: {name}')
        self._increment()

        val = self._currentToken()
        try:
            # try to parse val as int
            val = int(val, 10)
            self._increment()
            setattr(obj, name, val)
        except ValueError:
            # Try float
            try:
                val = float(val)
                self._increment()
                setattr(obj, name, val)
            except ValueError:
                # otherwise try to parse val as string
                if not val.startswith('"'):
                    raise GMLParseException(f'[pos {self._i}] attribute name is not alphanumeric: {name}')

                val_l = []
                while not self._currentToken().endswith('"'):
                    val_l.append(self._currentToken())
                    self._increment()
                val_l.append(self._currentToken())  # capture closing one

                self._increment()

                val = ' '.join(val_l)  # unify
                val = val.strip('"')
                setattr(obj, name, val)

        return obj

    def _parseOpenWithKeyword(self, kw):
        if self._currentToken() != kw:
            raise GMLParseException(f'[pos {self._i}] expected `{kw}` keyword, found: {self._currentToken()}')
        self._increment()

        if self._currentToken() != '[':
            raise GMLParseException(f'[pos {self._i}] expected opening [, found: {self._currentToken()}')
        self._increment()
