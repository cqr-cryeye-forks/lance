#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-16 11:29:29
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

import argparse
import sys


def cmdLineParser():
    parser = argparse.ArgumentParser(description='lance. By b4zinga@outlook.com',
                                     usage='python lance.py')
    target = parser.add_argument_group("Target")
    target.add_argument(
        "--target",
        metavar="URL",
        dest="target",
        type=str,
        help="target url.",
    )

    module = parser.add_argument_group("Module")
    module.add_argument(
        "--module",
        metavar="module",
        dest="module",
        type=str,
        default='',
        help="poc or exp to be loaded. defaul is all.",
    )

    if len(sys.argv) == 1:
        sys.argv.append('-h')

    args = parser.parse_args()
    return args
