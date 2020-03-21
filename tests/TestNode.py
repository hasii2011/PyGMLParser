
from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import expectedFailure
from unittest import main as unitTestMain

from org.hasii.pygmlparser.exceptions.GMLParseException import GMLParseException
from tests.TestBase import TestBase

from org.hasii.pygmlparser.Node import Node


class TestNode(TestBase):

    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestNode.clsLogger = getLogger(__name__)

    def setUp(self):
        self.logger: Logger = TestNode.clsLogger
        self.node:   Node   = Node()

    def tearDown(self):
        pass

    @expectedFailure
    def testOnlyInitialized(self):
        self.node.validate(22)

    @expectedFailure
    def testBadId(self):

        self.node.id = 'bogus'
        self.node.validate(22)

    def testGoodId(self):

        try:
            self.node.id = 27
            self.node.validate(22)
        except GMLParseException as e:
            self.fail(f'Should not get an exception: {e}')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestNode))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
