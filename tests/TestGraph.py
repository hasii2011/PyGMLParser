
from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import expectedFailure
from unittest import main as unitTestMain

from org.hasii.pygmlparser.Node import Node
from tests.TestBase import TestBase

from org.hasii.pygmlparser.Graph import Graph


class TestGraph(TestBase):

    FAIL_NODE_ID: int = 1

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestGraph.clsLogger = getLogger(__name__)

    def setUp(self):
        self.logger: Logger = TestGraph.clsLogger
        self.graph:  Graph  = Graph()

    def tearDown(self):
        pass

    def testBasicValidate(self):
        self.graph.validate(rawIdx=22, nodeId=0)

    @expectedFailure
    def testNodeAlreadyExist(self):

        failNode: Node = Node()
        failNode.id = TestGraph.FAIL_NODE_ID
        self.graph.graphNodes[TestGraph.FAIL_NODE_ID] = failNode

        self.graph.validate(rawIdx=22, nodeId=TestGraph.FAIL_NODE_ID)


if __name__ == '__main__':
    unitTestMain()
