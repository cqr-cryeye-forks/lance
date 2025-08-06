from typing import Optional

import requests

from lib.log import logger


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    target_url = f"{address}/info"
    try:
        logger.info(f"Checking Docker API at {target_url}")
        response = requests.get(target_url, verify=False, timeout=5)
        if "Containers" in response.text:
            logger.success("Docker Remote API unauth Vulnerable")
            logger.info(f"Response: {response.text}")
            return "Docker Remote API unauth Vulnerable"
        logger.warning("No 'Containers' found in response")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
