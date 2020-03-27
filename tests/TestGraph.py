
from logging import Logger
from logging import getLogger

from pytest import fixture
from pytest import raises

from pygmlparser.exceptions.GMLParseException import GMLParseException
from tests.TestBase import TestBase

from pygmlparser.Node import Node

from pygmlparser.Graph import Graph


FAIL_NODE_ID: int = 1


@fixture(name='moduleLogger')
def setUpClass():
    TestBase.setUpLogging()
    moduleLogger: Logger = getLogger(__name__)

    return moduleLogger


@fixture(name='graph')
def setUpGraph():
    graph: Graph = Graph()
    return graph


def testBasicValidate(graph):
    graph.validate(rawIdx=22, nodeId=0)


def testNodeAlreadyExists(graph):

    failNode: Node = Node()
    failNode.id = FAIL_NODE_ID
    graph.graphNodes[FAIL_NODE_ID] = failNode
    with raises(expected_exception=GMLParseException):
        graph.validate(rawIdx=22, nodeId=FAIL_NODE_ID)
