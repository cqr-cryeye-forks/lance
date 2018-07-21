#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-11 14:31:31
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :
import os
import importlib
from lib.data import logger


def loadPlugin(url, poc=None):
    """load all plugins.
    """
    if "://" not in url:
        url = "http://" + url
    url = url.strip("/")
    logger.info("Target url: %s" % url)

    plugin_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"plugins")
    if not os.path.isdir(plugin_path):
        logger.warning("%s is not a directory! " % plugin_path)
        raise EnvironmentError
    logger.info("Plugin path: %s " % plugin_path)
    
    items = os.listdir(plugin_path)
    if poc:
        logger.infxito("Loading %s plugins." % poc)
    else:
        poc=""
    for item in items:
        if item.endswith(".py") and not item.startswith('__'):
            plugin_name = item[:-3]
            if poc in plugin_name:
                logger.info("Loading plugin: %s" % plugin_name)

                module = importlib.import_module("plugins." + plugin_name)

                try:
                    result = module.run(url)
                    if result:
                        logger.success(result)
                    else:
                        logger.error("Not Vulnerable %s " % plugin_name)
                except:
                    logger.warning("ConnectionError ")
            else:
                continue

    logger.info("Finished")