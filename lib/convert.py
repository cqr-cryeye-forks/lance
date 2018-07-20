#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-20 16:35:54
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import os
import sys

UNICODE_ENCODING = 'utf-8'

def stdoutencode(data):
    retVal = None

    try:
        data = data or ""

        # Reference: http://bugs.python.org/issue1602
        if os.name == 'nt':
            output = data.encode(sys.stdout.encoding, "replace")
            output = output.decode()
            # print(output, type(output))
            if '?' in output and '?' not in data:
                warnMsg = "cannot properly display Unicode characters "
                warnMsg += "inside Windows OS command prompt "
                warnMsg += "(http://bugs.python.org/issue1602). All "
                warnMsg += "unhandled occurances will result in "
                warnMsg += "replacement with '?' character. Please, find "
                warnMsg += "proper character representation inside "
                warnMsg += "corresponding output files. "
                singleTimeWarnMessage(warnMsg)

            retVal = output
        else:
            retVal = data.encode(sys.stdout.encoding)
    except:
        retVal = data.encode(UNICODE_ENCODING) if isinstance(data, unicode) else data

    return retVal
