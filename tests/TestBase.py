
import os
import json
import logging
import logging.config

from unittest import TestCase

JSON_LOGGING_CONFIG_FILENAME = "testLoggingConfig.json"


class TestBase(TestCase):
    """
    A base unit test class to initialize some logging stuff we need
    """

    @classmethod
    def setUpLogging(cls):
        """"""
        loggingConfigFilename: str = cls.findLoggingConfig()

        with open(loggingConfigFilename, 'r') as loggingConfigurationFile:
            configurationDictionary = json.load(loggingConfigurationFile)

        logging.config.dictConfig(configurationDictionary)
        logging.logProcesses = False
        logging.logThreads = False

    @classmethod
    def findLoggingConfig(cls) -> str:
        """"""
        from os import getcwd

        upDir = f'tests/{JSON_LOGGING_CONFIG_FILENAME}'
        if os.path.isfile(upDir):
            return upDir

        if os.path.isfile(JSON_LOGGING_CONFIG_FILENAME):
            return JSON_LOGGING_CONFIG_FILENAME
        else:
            os.chdir("../")
            return cls.findLoggingConfig()