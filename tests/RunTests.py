
import unittest
from unittest import TestSuite
from unittest import TestLoader

from tests import TestParser
from tests import TestNode


def main():
    # Initialize the test suite
    testLoader: TestLoader = unittest.TestLoader()
    suite: TestSuite = unittest.TestSuite()

    suite.addTest(testLoader.loadTestsFromTestCase(TestParser))
    suite.addTest(testLoader.loadTestsFromTestCase(TestNode))

    # initialize a runner, pass it our suite and run it
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    print(result)


if __name__ == '__main__':
    main()
