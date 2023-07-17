#!/usr/bin/python3

import sys
import os

domain = sys.argv[1]

def crtsh():
    crtsh_command = f"crtsh {domain} | anew crtsh.subs"
    os.system(crtsh_command)

crtsh()
