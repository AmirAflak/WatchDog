#!/usr/bin/python3

import os
from typing import Generator
from configs import DOMAIN

def findomain() -> Generator[str, None, None]:
    findomain_command = f'findomain -t {DOMAIN} -q 2>/dev/null'
    
    for line in os.popen(crtsh_command):
        yield line.strip()

# for line in findomain():
#     print(line)

__all__ = ['findomain']

