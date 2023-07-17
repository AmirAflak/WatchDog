#!/usr/bin/python3

import os
from typing import Generator


def findomain(domain: str) -> Generator[str, None, None]:
    findomain_command = f'findomain -t {domain} -q 2>/dev/null'
    
    for line in os.popen(crtsh_command):
        yield line.strip()

# domain = 'caterpillar.com'
# for line in findomain(domain):
#     print(line)

__all__ = ['findomain']

