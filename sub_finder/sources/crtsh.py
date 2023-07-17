#!/usr/bin/python3

import os
from typing import Generator
from configs import DOMAIN

def crtsh() -> Generator[str, None, None]:
    crtsh_command = f"crtsh {DOMAIN}"
    for line in os.popen(crtsh_command):
        yield line.strip()

# for line in crtsh():
#     print(line)

__all__ = ['crtsh']
