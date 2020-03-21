
from logging import Logger
from logging import getLogger

from pytest import fixture
# from pytest import raises     # in case you need it

from tests.TestBase import TestBase

# import the class you want to test here

"""
You need to change the name of this class to Test`xxxx`
Where `xxxx' is the name of the class that you want to test.

See existing tests for more information.
"""


@fixture(name='moduleLogger')
def setUpClass():
    TestBase.setUpLogging()
    moduleLogger: Logger = getLogger(__name__)

    return moduleLogger


@fixture(name='MAKE UP A NAME')
def setUp():
    # Setup test data
    pass


def testName1(moduleLogger):
    moduleLogger.info(f'I am test 1')


def testName2(moduleLogger):
    moduleLogger.info(f'I am test 1')
