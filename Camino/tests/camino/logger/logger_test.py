import unittest
from tests.camino.context import log


class TestLogger(unittest.TestCase):

    def test_debug(self):
        with self.assertLogs(level='DEBUG') as lc:
            log.message("debug",'This is a debug message')
            self.assertEqual(['DEBUG:root:logger_test.py/test_debug:9 - This is a debug message'], lc.output)

    def test_info(self):
        with self.assertLogs(level='INFO') as lc:
            log.message("info",'This is a info message')
            self.assertEqual(['INFO:root:logger_test.py/test_info:14 - This is a info message'], lc.output)

    def test_warning(self):
        with self.assertLogs(level='WARNING') as lc:
            log.message("warning",'This is a warning message')
            self.assertEqual(['WARNING:root:logger_test.py/test_warning:19 - This is a warning message'], lc.output)

    def test_error(self):
        with self.assertLogs(level='ERROR') as lc:
            log.message("error",'This is a error message')
            self.assertEqual(['ERROR:root:logger_test.py/test_error:24 - This is a error message'], lc.output)

    def test_critical(self):
        with self.assertLogs(level='CRITICAL') as lc:
            log.message("critical",'This is a critical message')
            self.assertEqual(['CRITICAL:root:logger_test.py/test_critical:29 - This is a critical message'], lc.output)

    def test_unknown(self):
        with self.assertLogs() as lc:
            log.message("unknown",'This is a unknown message')
            self.assertEqual(['INFO:root:logger_test.py/test_unknown:34 - This is a unknown message'], lc.output)

