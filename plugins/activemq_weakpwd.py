#!/usr/bin/env python
# coding: utf-8
# Date  : 2025-08-05 14:45
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  : Detect weak password vulnerability in ActiveMQ

import base64
from typing import Optional

import requests

from lib.log import logger


def get_auth_header(username: str, password: str) -> str:
    """Generate Basic Auth header."""
    credentials = f"{username}:{password}"
    return f"Basic {base64.b64encode(credentials.encode()).decode()}"


def run(url: str) -> Optional[str]:
    """Detect weak password vulnerability in ActiveMQ."""
    # Ensure admin endpoint is included
    if ":8161" in url:
        target_url = f"{url}/admin/"
    else:
        target_url = f"{url}:8161/admin/"

    # List of weak credentials to test
    weak_credentials = [
        "admin", "s3cret", "password", "p@ssw0rd", "1qaz2wsx", "root", "activemq", "ActiveMQ"
    ]

    for user in weak_credentials:
        for pwd in weak_credentials:
            headers = {'Authorization': get_auth_header(user, pwd)}
            try:
                logger.info(f"Testing credentials: {user}:{pwd}")
                response = requests.get(target_url, headers=headers, timeout=5, verify=False)
                if "Unauthorized" not in response.text:
                    msg = f"ActiveMQ weak password!\t{target_url}\tusername:{user}, pwd:{pwd}"
                    logger.success(msg)
                    return msg
                logger.warning(f"Unauthorized with {user}:{pwd}")
            except requests.RequestException as e:
                logger.error(f"Request failed for {user}:{pwd}: {str(e)}")
            except Exception as e:
                logger.error(f"Unexpected error for {user}:{pwd}: {str(e)}")

    logger.warning("No weak passwords found")
    return None


if __name__ == "__main__":
    # Example usage
    print(run("localhost"))
