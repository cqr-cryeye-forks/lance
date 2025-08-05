import sys
import logging
from lib.ansistrm import ColorizingStreamHandler


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


def setup_logger(disable_color=False):
    if disable_color:
        handler = logging.StreamHandler(sys.stdout)
    else:
        handler = ColorizingStreamHandler(sys.stdout)
        handler.level_map[logging.getLevelName("*")] = (None, "cyan", False)
        handler.level_map[logging.getLevelName("+")] = (None, "red", False)
        handler.level_map[logging.getLevelName("-")] = (None, "green", False)
        handler.level_map[logging.getLevelName("!")] = (None, "yellow", False)

    formatter = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(CustomLogging.WARNING)
    return LOGGER


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


logger = setup_logger(disable_color="--disable-col" in sys.argv)
