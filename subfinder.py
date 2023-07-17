#!/usr/bin/python3

import os
from typing import Generator


def subfinder():
    subfinder_command = f"subfinder -d {domain} -all"
    for line in os.popen(subfinder_command):
        yield line.strip()
        
    
# domain = 'caterpillar.com'
# for line in subfinder(domain):
#     print(line)
