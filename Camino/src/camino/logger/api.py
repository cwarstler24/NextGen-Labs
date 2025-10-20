
import logging.config
import yaml
from enum import Enum
from inspect import getframeinfo, stack
import pathlib
from src.camino.config.setting import Settings


class Level(Enum):
    DEBUG = 0
    WARNING = 1
    INFO = 2
    ERROR = 3
    CRITICAL = 4


class _Logger(object):
    """
    This is the class that encapsulates the Log actions.

    This is intended to be a private class exposed thru the module
    __init__.py.
    """

    def __init__(self) -> None:
        """
        This is the constructor for the Log object.

        It reads the loger.yaml file from the config module of the Camino
        application.
        """

        config_name = Settings.logger_config_file()

        with open(config_name, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        self.logger = logging.getLogger()

    def message(self, level: Level, message: str) -> None:
        """
        This is the action method for the Log object.

        Log levels (in ascending order) are:
          Level.DEBUG
          Level.INFO
          Level.WARNING
          Level.ERROR
          Level.CRITICAL

        the default log level is 'info'.

        :param level: The log level to use.
        :param message: The message to log.
        :return: None.
        """

        caller = getframeinfo(stack()[1][0])
        path = pathlib.PurePath(caller.filename)
        parts = path.parts
        start = parts.index("Camino") + 1
        package_name = '/'.join(parts[start:-1])
        output = "{}/{}/{}:{} - {}".format(package_name, path.stem, caller.function, caller.lineno, message)
        if level == Level.DEBUG:
            self.logger.debug(output)
        elif level == Level.INFO:
            self.logger.info(output)
        elif level == Level.WARNING:
            self.logger.warning(output)
        elif level == Level.ERROR:
            self.logger.error(output)
        elif level == Level.CRITICAL:
            self.logger.critical(output)
        else:
            self.logger.info(output)
