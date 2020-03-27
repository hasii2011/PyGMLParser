
from typing import cast
from typing import List
from typing import NewType
from typing import Tuple
from typing import Union

from logging import Logger
from logging import getLogger

from pygmlparser.Edge import Edge
from pygmlparser.Graph import Graph
from pygmlparser.Node import Node

from pygmlparser.graphics.Point import Point
from pygmlparser.graphics.EdgeGraphics import EdgeGraphics
from pygmlparser.graphics.NodeGraphics import NodeGraphics

from pygmlparser.exceptions.GMLParseException import GMLParseException


class Parser:

    AttrObjectType = NewType('AttrObjectType', Union[Node, Edge, NodeGraphics, EdgeGraphics, Point])
    LineType       = NewType('LineType', Tuple[Point, ...])

    GRAPH_TOKEN: str = 'graph'

    ID_TOKEN:   str = 'id'
    NODE_TOKEN: str = 'node'
    EDGE_TOKEN: str = 'edge'

    SOURCE_ID_TOKEN: str = 'source'
    TARGET_ID_TOKEN: str = 'target'

    GRAPHICS_TOKEN: str = 'graphics'
    START_TOKEN:    str = '['
    END_TOKEN:      str = ']'

    QUOTE_TOKEN: str = '"'

    LINE_DEFINITION_TOKEN:  str = 'Line'
    POINT_DEFINITION_TOKEN: str = 'point'

    def __init__(self):
        self.logger: Logger    = getLogger(__name__)
        self._raw:   List[str] = []
        """
        raw GML data (raw string split on whitespace)
        """
        self._i: int = 0
        """
        position (index) in self._raw
        """

        self.graph: Graph = cast(Graph, None)

    def loadGML(self, path: str):
        """
        First method to call after instantiating a Graph object

        Args:
            path: The fully qualified path to the .gml file

        """
        with open(path) as infile:
            # NOTE: the split will destroy any spaces in string attributes
            self._raw = infile.read().strip().split()

        self._i    = 0
        self.graph = Graph()

    def parse(self):
        """
        The second method to call after the parser loads the .gml file.  After this
        method completes extract the graph from `org.hasii.pygmlparser.Graph`

        """
        if len(self._raw) == 0:
            raise GMLParseException('Mot loaded you must call load_gml before parse')

        self._parseGraph()

    def _currentToken(self) -> str:
        if self._i >= len(self._raw):
            raise GMLParseException(f'[pos {self._i}] unexpected end of file')

        return self._raw[self._i]

    def _increment(self):
        self._i += 1

    def _parseGraph(self):
        self._parseOpenWithKeyword(Parser.GRAPH_TOKEN)

        while self._currentToken() != Parser.END_TOKEN:
            currentToken = self._currentToken()
            self.logger.debug(f'currentToken: {currentToken}')
            if currentToken == Parser.NODE_TOKEN:
                self._parseNode()
            elif currentToken == Parser.EDGE_TOKEN:
                self._parseEdge()
            else:
                self._parseAttribute(self.graph)
        self._increment()

    def _parseNode(self):
        self._parseOpenWithKeyword(Parser.NODE_TOKEN)

        node = Node()

        while self._currentToken() != Parser.END_TOKEN:
            try:
                current: str = self._currentToken()
                if current == Parser.GRAPHICS_TOKEN:
                    self._parseNodeGraphics(node)
                else:
                    self._parseAttribute(node)
            except GMLParseException:
                self.logger.error(f'current: {self._currentToken()}')
                continue
        self.logger.debug(f'Current index: {self._i}')
        self._increment()

        node.validate(rawIdx=self._i)
        nid = node.id
        self.graph.validate(rawIdx=self._i, nodeId=nid)

        self.logger.info(f'Parsed Node: {node}')
        self.graph.graphNodes[nid] = node

    def _parseEdge(self):
        self._parseOpenWithKeyword(Parser.EDGE_TOKEN)

        edge: Edge = Edge()

        while self._currentToken() != Parser.END_TOKEN:
            current: str = self._currentToken()
            if current == Parser.GRAPHICS_TOKEN:
                self._parseEdgeGraphics(edge)
            else:
                self._parseAttribute(edge)
        self._increment()
        edge.validate(rawIdx=self._i)

        for nid in (edge.source, edge.target):
            if nid not in self.graph.graphNodes:
                node: Node = Node()
                node.is_anon = True
                node.id = nid
                self.graph.graphNodes[nid] = node

        edge.source_node = self.graph.graphNodes[edge.source]
        edge.target_node = self.graph.graphNodes[edge.target]

        edge.source_node.forward_edges.append(edge)
        edge.target_node.backward_edges.append(edge)

        self.logger.info(f'Parsed Edge: {edge}')
        self.graph.graphEdges.append(edge)

    def _parseNodeGraphics(self, node: Node):

        self._parseOpenWithKeyword(Parser.GRAPHICS_TOKEN)
        graphics: NodeGraphics = NodeGraphics()

        while self._currentToken() != Parser.END_TOKEN:
            self._parseAttribute(graphics)

        self._increment()
        self.logger.debug(f'Current index: {self._i}')
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
            self.logger.debug(f'current: {current}')

            lineList = self._parsePointDefinition(lineList)

        # But the data classes save a line definition as a Tuple of points
        graphics.line = tuple(lineList)

        self._increment()
        return graphics

    def _parsePointDefinition(self, lineList: List[Point]) -> List[Point]:

        self._parseOpenWithKeyword(Parser.POINT_DEFINITION_TOKEN)

        point: Point = Point()
        while self._currentToken() != Parser.END_TOKEN:
            self.logger.debug(f'point current: {self._currentToken()}')
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
                if not val.startswith(f'{Parser.QUOTE_TOKEN}'):
                    raise GMLParseException(f'[pos {self._i}] attribute name is not alphanumeric: {name}')

                val_l = []
                while not self._currentToken().endswith(f'{Parser.QUOTE_TOKEN}'):
                    val_l.append(self._currentToken())
                    self._increment()
                val_l.append(self._currentToken())  # capture closing one

                self._increment()

                val = ' '.join(val_l)  # unify
                val = val.strip(f'{Parser.QUOTE_TOKEN}')
                setattr(obj, name, val)

        return obj

    def _parseOpenWithKeyword(self, kw: str):
        if self._currentToken() != kw:
            raise GMLParseException(f'[pos {self._i}] expected `{kw}` keyword, found: {self._currentToken()}')
        self._increment()

        if self._currentToken() != Parser.START_TOKEN:
            raise GMLParseException(f'[pos {self._i}] expected opening `[`, found: {self._currentToken()}')
        self._increment()
