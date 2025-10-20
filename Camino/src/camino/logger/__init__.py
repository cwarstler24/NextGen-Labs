"""
 This is the Logging module for the Camino application.

 The log object exposed in this module is a singleton
 pattern to ensure only one loger will exist for all the modules to use.

 The logging config file is camino/config/logger.yaml, the default log file
 is camino/camino.log.

"""

from .api import _Logger

log = _Logger()