#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-20 10:29:03
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import sys
import logging

class CustomLogging:
    SYSINFO = 9
    SUCCESS = 8
    ERROR = 7
    WARNING = 6


logging.addLevelName(CustomLogging.SYSINFO, "*")
logging.addLevelName(CustomLogging.SUCCESS, "+")
logging.addLevelName(CustomLogging.ERROR, "-")
logging.addLevelName(CustomLogging.WARNING, "!")

LOGGER = logging.getLogger("lanceLog")

LOGGER_HANDLER = None
try:
    from lib.ansistrm import ColorizingStreamHandler

    disableColor = False

    for argument in sys.argv:
        if "disable-col" in argument:
            disableColor = True
            break

    if disableColor:
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
    else:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
        LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "red", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "green", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
except ImportError as e:
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(CustomLogging.WARNING)


class MyLogger:
    @staticmethod
    def success(msg):
        return LOGGER.log(CustomLogging.SUCCESS, msg)

    @staticmethod
    def info(msg):
        return LOGGER.log(CustomLogging.SYSINFO, msg)

    @staticmethod
    def warning(msg):
        return LOGGER.log(CustomLogging.WARNING, msg)

    @staticmethod
    def error(msg):
        return LOGGER.log(CustomLogging.ERROR, msg) 