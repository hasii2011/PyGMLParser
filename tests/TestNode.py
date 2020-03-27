
from logging import Logger
from logging import getLogger

from pytest import fixture
from pytest import raises

from tests.TestBase import TestBase

from pygmlparser.Node import Node
from pygmlparser.exceptions.GMLParseException import GMLParseException


@fixture(name='moduleLogger')
def setUpClass():
    TestBase.setUpLogging()
    moduleLogger: Logger = getLogger(__name__)

    return moduleLogger


@fixture(name='node')
def setUp():

    node: Node   = Node()
    return node


def testOnlyInitialized(node):
    with raises(expected_exception=GMLParseException):
        node.validate(22)


def testBadId(node):

    node.id = 'bogus'
    with raises(expected_exception=GMLParseException):
        node.validate(22)


def testGoodId(node):

    try:
        node.id = 27
        node.validate(22)
    except GMLParseException as e:
        assert False, f'Should not get an exception: {e}'
