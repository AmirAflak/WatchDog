#!/usr/bin/python3

import sys
import os

domain = sys.argv[1]

def assetfinder():
    assetfinder_command = f'assetfinder --subs-only {domain} | anew assetfinder.subs'
    os.system(assetfinder_command)

assetfinder()

