
from logging import Logger
from logging import getLogger

from os import sep as osSep
from os import path as osPath
from os import chdir as osChdir

from pytest import fixture

from tests.TestBase import TestBase

from pygmlparser.graphics.NodeGraphics import NodeGraphics

from pygmlparser.Edge import Edge
from pygmlparser.Node import Node
from pygmlparser.Parser import Parser
from pygmlparser.Graph import Graph


EXPECTED_NODE_COUNT: int = 5
EXPECTED_EDGE_COUNT: int = 4

EXPECTED_EDGE_0_SOURCE_ID: int = 0
EXPECTED_EDGE_0_TARGET_ID: int = 1

NODE_2_ID: int = 2

EXPECTED_NODE_2_X: int = -150
EXPECTED_NODE_2_Y: int = -527

TEST_FILES_DIR:            str = 'testfiles'
MONOLITHIC_TEST_FILE_NAME: str = 'hasiiGraph.gml'

RELATIVE_TEST_FILE_DIR: str = f'{TEST_FILES_DIR}{osSep}{MONOLITHIC_TEST_FILE_NAME}'


@fixture(name='moduleLogger')
def setUpLogging():
    TestBase.setUpLogging()
    moduleLogger: Logger = getLogger(__name__)

    return moduleLogger


@fixture(name='parser')
def setUp():
    parser: Parser = Parser()
    return parser


@fixture(name='monolithTestFilePath')
def _findMonolithicTestFile() -> str:

    upDir = f'tests{osSep}{RELATIVE_TEST_FILE_DIR}'
    if osPath.isfile(upDir):
        return upDir

    if osPath.isfile(RELATIVE_TEST_FILE_DIR):
        return RELATIVE_TEST_FILE_DIR
    else:
        osChdir("../")
        return _findMonolithicTestFile()


def testMonolithic(parser, monolithTestFilePath, moduleLogger):
    """
    Not really a good test since it parses an entire file and then inspects sub-aspects.  However,
    as I find bugs in various protected methods I will fill it in.
    """
    parser.loadGML(monolithTestFilePath)
    parser.parse()

    graph: Graph = parser.graph

    actualNodeCount: int = len(graph.graphNodes)
    assert EXPECTED_NODE_COUNT == actualNodeCount, 'Mismatch on parsed nodes'

    actualEdgeCount: int = len(graph.graphEdges)
    assert EXPECTED_EDGE_COUNT == actualEdgeCount, 'Mismatch on parsed edges'

    edge0: Edge = graph.graphEdges[0]
    actualEdge0SourceId: int = edge0.source
    actualEdge0TargetId: int = edge0.target

    assert EXPECTED_EDGE_0_SOURCE_ID == actualEdge0SourceId, 'Source structure might have changed'
    assert EXPECTED_EDGE_0_TARGET_ID == actualEdge0TargetId, 'Target structure might have changed'

    node2:         Node         = graph.graphNodes[NODE_2_ID]
    node2Graphics: NodeGraphics = node2.graphics
    actualX: int = node2Graphics.x
    actualY: int = node2Graphics.y

    assert EXPECTED_NODE_2_X == actualX, 'X position not correctly parsed'
    assert EXPECTED_NODE_2_Y == actualY, 'Y position not correctly parsed'

    moduleLogger.debug(f'graph: {graph}')
