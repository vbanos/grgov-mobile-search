# -*- coding: utf-8 -*-
## @author Vangelis Banos
"""
Main Configuration File
"""
import logging

DEBUG = True

PORT = 3000
BASE_URL = "http://m.yperdiavgeia.gr/"

ROOT_DIR = "/var/www/m.yperdiavgeia.gr/"

# LOGGING
LOG_DIR = ROOT_DIR + "logs/"
LOG_ROTATION_SIZE = 1000000 # 1 MB
# position of UPDATE in the hierarchy of log levels
UPDATE_LEVEL = logging.WARNING
# string containing the format of the logs in the same form as python's logging.Formatter
LOG_FORMAT = '%(levelname)s::%(asctime)s::%(name)s -  - %(message)s'
LOG_LEVEL = logging.WARNING

ERROR_LOG_NAME = "error.log"
ACCESS_LOG_NAME = "access.log"
UPDATE_LOG_NAME = "update.log"
# END LOGGING

DECISIONS_URL = "http://yperdiavgeia.gr/decisions/opensearch/"

PROCUREMENTS_URL = "http://yperdiavgeia.gr/procurements/opensearch/"

LAWS_URL = "http://yperdiavgeia.gr/laws/opensearch/"
