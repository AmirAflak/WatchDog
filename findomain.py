#!/usr/bin/python3

import sys
import os

domain = sys.argv[1]


def findomain():
    findomain_command = f'findomain -t {domain} -q 2>/dev/null | anew findomain.subs'
    os.system(findomain_command)

findomain()

