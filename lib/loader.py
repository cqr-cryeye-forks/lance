import importlib

from lib.constants import PLUGINS_DIR, PLUGIN_CONFIG, keywords
from lib.log import logger


# def load_plugin(url: str) -> list[str]:
#     results: list[str] = []
#
#     url = _normalize_url(url)
#     _check_plugins_directory()
#
#     for plugin_name, func_name in PLUGIN_CONFIG:
#         try:
#             module = importlib.import_module(f"plugins.{plugin_name}")
#             result: str = getattr(module, func_name)(url)
#             entry = _handle_plugin_result(plugin_name, result, results)
#             if entry:
#                 results.append(entry)
#         except Exception as e:
#             logger.warning(f"Error running plugin {plugin_name}: {e}")
#
#     logger.info("Finished")
#     return results

def load_plugin(url):
    results: list[str] = []

    url = _normalize_url(url)
    _check_plugins_directory()

    for plugin_name, func_name in PLUGIN_CONFIG:
        try:
            # Dynamically import the plugin module
            module = importlib.import_module(f"plugins.{plugin_name}")
            # Call the specified function
            result = getattr(module, func_name)(url)
            if result:
                logger.success(result)
            else:
                logger.error(f"Not Vulnerable {plugin_name}")
            if (
                    (result not in results) and
                    (result not in keywords) and
                    result
            ):
                results.append(f"{result} 111")
            if result not in results:
                results.append(f"{result} 222")
            if isinstance(result, str):
                results.append(f"{result} 333")

        except Exception as e:
            logger.warning(f"Error running plugin {plugin_name}: {e}")

    logger.info("Finished")
    return results


def _normalize_url(url: str) -> str:
    if "://" not in url:
        url = "http://" + url
    url = url.strip("/")
    logger.info(f"Target url: {url}")
    return url


def _check_plugins_directory() -> None:
    if not PLUGINS_DIR.is_dir():
        logger.warning(f"{PLUGINS_DIR} is not a directory!")
        raise EnvironmentError
    logger.info(f"Plugin path: {PLUGINS_DIR}")


def _handle_plugin_result(plugin_name: str, result: str | bool, results: list[str]) -> str | None:
    if result in keywords:
        return None

    if isinstance(result, str):
        if result in results:
            return None
        if result:
            logger.success(result)
        else:
            logger.error(f"Not Vulnerable {plugin_name}")
        return result
    return None
