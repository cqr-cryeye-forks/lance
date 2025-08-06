import socket
from typing import Optional

from lib.log import logger
from plugins.package.payloads import payload_redis_unauth_1


def run(url: str, port: int) -> Optional[str]:
    payload = payload_redis_unauth_1
    ip = url.split("://")[-1] if "://" in url else url
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.connect((ip, port))
            s.send(payload.encode())
            recvdata = s.recv(1024)
            if recvdata and 'redis_version' in recvdata.decode(errors='ignore'):
                logger.success("Redis unauth Vulnerable")
                return "Redis unauth Vulnerable"
            logger.warning("No redis_version found in response")
            return None
    except socket.error as e:
        logger.error(f"Socket error: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None
