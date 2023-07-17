#!/usr/bin/python3

import os
from typing import Generator


def crtsh(domain: str) -> Generator[str, None, None]:
    crtsh_command = f"crtsh {domain}"
    for line in os.popen(crtsh_command):
        yield line.strip()

# domain = 'caterpillar.com'
# for line in crtsh(domain):
#     print(line)
