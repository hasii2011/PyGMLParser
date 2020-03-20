
from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import main as unitTestMain

from os import sep as osSep
from os import path as osPath
from os import chdir as osChdir

from org.hasii.pygmlparser.Edge import Edge
from org.hasii.pygmlparser.Node import Node
from org.hasii.pygmlparser.graphics.NodeGraphics import NodeGraphics

from tests.TestBase import TestBase

from org.hasii.pygmlparser.Parser import Parser
from org.hasii.pygmlparser.Parser import Graph


class TestGMLParser(TestBase):

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
    """
    """
    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestGMLParser.clsLogger = getLogger(__name__)

    def setUp(self):
        self.logger: Logger = TestGMLParser.clsLogger
        self.parser: Parser = Parser()

        self._monolithTestFilePath: str = self._findMonolithicTestFile()

    @classmethod
    def _findMonolithicTestFile(cls) -> str:
        upDir = f'tests{osSep}{TestGMLParser.RELATIVE_TEST_FILE_DIR}'
        if osPath.isfile(upDir):
            return upDir

        if osPath.isfile(TestGMLParser.RELATIVE_TEST_FILE_DIR):
            return TestGMLParser.RELATIVE_TEST_FILE_DIR
        else:
            osChdir("../")
            return cls.findLoggingConfig()

    def tearDown(self):
        pass

    def testMonolithic(self):
        """
        Not really a good test since it parses an entire file and then inspects sub-aspects.  However,
        as I find bugs in various protected methods I will fill it in.
        """
        self.parser.loadGML(self._findMonolithicTestFile())
        self.parser.parse()

        graph: Graph = self.parser.graph

        actualNodeCount: int = len(graph.graphNodes)
        self.assertEqual(TestGMLParser.EXPECTED_NODE_COUNT, actualNodeCount, 'Mismatch on parsed nodes')

        actualEdgeCount: int = len(graph.graphEdges)
        self.assertEqual(TestGMLParser.EXPECTED_EDGE_COUNT, actualEdgeCount, 'Mismatch on parsed edges')

        edge0: Edge = graph.graphEdges[0]
        actualEdge0SourceId: int = edge0.source
        actualEdge0TargetId: int = edge0.target

        self.assertEqual(TestGMLParser.EXPECTED_EDGE_0_SOURCE_ID, actualEdge0SourceId, 'Source structure might have changed')
        self.assertEqual(TestGMLParser.EXPECTED_EDGE_0_TARGET_ID, actualEdge0TargetId, 'Target structure might have changed')

        node2:         Node         = graph.graphNodes[TestGMLParser.NODE_2_ID]
        node2Graphics: NodeGraphics = node2.graphics
        actualX: int = node2Graphics.x
        actualY: int = node2Graphics.y

        self.assertEqual(TestGMLParser.EXPECTED_NODE_2_X, actualX, 'X position not correctly parsed')
        self.assertEqual(TestGMLParser.EXPECTED_NODE_2_Y, actualY, 'Y position not correctly parsed')

        self.logger.debug(f'graph: {graph}')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestGMLParser))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
