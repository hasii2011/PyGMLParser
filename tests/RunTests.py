
import unittest
from unittest import TestSuite
from unittest import TestLoader

from tests.TestGMLParser import TestGMLParser


def main():
    # Initialize the test suite
    testLoader: TestLoader = unittest.TestLoader()
    suite: TestSuite = unittest.TestSuite()

    suite.addTest(testLoader.loadTestsFromTestCase(TestGMLParser))

    # initialize a runner, pass it our suite and run it
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    print(result)


if __name__ == '__main__':
    main()
