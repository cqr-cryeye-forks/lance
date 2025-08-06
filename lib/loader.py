import importlib

from lib.constants import PLUGINS_DIR, PLUGIN_CONFIG, keywords
from lib.log import logger


def load_plugin(url, port):
    results: list[str] = []

    url = _normalize_url(url)
    _check_plugins_directory()

    for plugin_name, func_name, port_list in PLUGIN_CONFIG:
        if port:
            port_list = [port]
        for port in port_list:
            try:
                # Dynamically import the plugin module
                module = importlib.import_module(f"plugins.{plugin_name}")
                # Call the specified function
                result = getattr(module, func_name)(url, port)
                if result:
                    logger.success(result)
                    results.append(f"{result} 111")
                    results.append("---")
                else:
                    msg = f"Not Vulnerable {plugin_name}"
                    logger.error(msg)
                    results.append(msg)
                    results.append(f"{result} 222")
                    results.append("---")

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
