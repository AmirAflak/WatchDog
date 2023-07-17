#!/usr/bin/python3

import os
import sys

domain = sys.argv[1]

def amass():
    amass_command = f'amass enum -passive -norecursive -noalts -d {domain} 2>/dev/null | anew amass.subs'
    os.system(amass_command)

amass()

