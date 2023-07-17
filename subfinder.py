#!/usr/bin/python3

import os
from typing import Generator
from configs import DOMAIN

def subfinder():
    subfinder_command = f"subfinder -d {DOMAIN} -all"
    for line in os.popen(subfinder_command):
        yield line.strip()
        
    
# for line in subfinder():
#     print(line)

__all__ = ['subfinder']
