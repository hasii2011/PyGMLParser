
from logging import Logger
from logging import getLogger

from pytest import fixture
from pytest import raises

from tests.TestBase import TestBase

from pygmlparser.Edge import Edge
from pygmlparser.exceptions.GMLParseException import GMLParseException


@fixture(name='moduleLogger')
def setUpModule():
    TestBase.setUpLogging()
    moduleLogger: Logger = getLogger(__name__)

    return moduleLogger


@fixture(name='edge')
def setUp():

    edge: Edge = Edge()

    return edge


def testPerfection(edge):

    try:
        edge.source = 1
        edge.target = 2
    except GMLParseException as e:
        assert False, f'Should not get an exception: {e}'


def testNoSource(edge):
    with raises(expected_exception=GMLParseException):
        edge.validate(22)


def testNoTarget(edge):
    edge.source = 1
    with raises(expected_exception=GMLParseException):
        edge.validate(22)


def testNonIntSource(edge):
    edge.source = ''
    with raises(expected_exception=GMLParseException):
        edge.validate(22)


def testNonIntTarget(edge):
    edge.source = 1
    edge.target = ''
    with raises(expected_exception=GMLParseException):
        edge.validate(22)
