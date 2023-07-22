#!/usr/bin/python3

import os
from typing import Generator
from configs import DOMAIN

def findomain(use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] findomain")
    if use_docker:
        findomain_command = f'docker run -it edu4rdshl/findomain:latest -t {DOMAIN} -q 2>/dev/null'
    else: 
        findomain_command = f'findomain -t {DOMAIN} -q 2>/dev/null'
    for line in os.popen(findomain_command):
        yield line.strip()

# for line in findomain():
#     print(line)

__all__ = ['findomain']

