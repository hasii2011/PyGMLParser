
from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import expectedFailure
from unittest import main as unitTestMain

from org.hasii.pygmlparser.exceptions.GMLParseException import GMLParseException
from tests.TestBase import TestBase

from org.hasii.pygmlparser.Edge import Edge


class TestEdge(TestBase):
    """
    """
    clsLogger: Logger = None

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestEdge.clsLogger = getLogger(__name__)

    def setUp(self):
        self.logger: Logger = TestEdge.clsLogger
        self.edge:   Edge   = Edge()

    def tearDown(self):
        pass

    def testPerfection(self):

        try:
            self.edge.source = 1
            self.edge.target = 2
        except GMLParseException as e:
            self.fail(f'Should not get an exception: {e}')

    @expectedFailure
    def testNoSource(self):
        self.edge.validate(22)

    @expectedFailure
    def testNoTarget(self):
        self.edge.source = 1
        self.edge.validate(22)

    @expectedFailure
    def testNonIntSource(self):
        self.edge.source = ''
        self.edge.validate(22)

    @expectedFailure
    def testNonIntTarget(self):
        self.edge.source = 1
        self.edge.target = ''
        self.edge.validate(22)


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestEdge))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
