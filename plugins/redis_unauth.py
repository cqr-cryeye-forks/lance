#!/usr/bin/env python
# coding: utf-8
# Date  : 2025-08-05 17:10
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  : Detect Redis unauthorized access vulnerability

import socket
from lib.log import logger
from typing import Optional

from plugins.package.payloads import payload_redis_unauth_1


def run(url: str) -> Optional[str]:
    """Detect Redis unauthorized access vulnerability."""
    payload = payload_redis_unauth_1
    ip = url.split("://")[-1] if "://" in url else url
    port = int(ip.split(':')[-1]) if ':' in ip else 6379

    try:
        logger.info(f"Connecting to Redis at {ip}:{port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(10)
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

if __name__ == "__main__":
    print(run("192.168.27.128"))