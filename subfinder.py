#!/usr/bin/python3

import sys
import os

domain = sys.argv[1]

def subfinder():
    subfinder_command = f"subfinder -d {domain} -all | anew subfinder.subs"
    os.system(subfinder_command)

subfinder()
