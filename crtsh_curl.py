#!/usr/bin/python3

import os
from typing import Generator


def crtsh_curl(domain: str) -> Generator[str, None, None]:
    command = f'curl -sk "https://crt.sh/?q=%.{domain}&output=json" | tr "," "\\n" | awk -F\'"\' \'/name_value/ {{gsub(/\\*\\./, "", $4); gsub(/\\\\n/,"\\n",$4);print $4}}\''
    for line in os.popen(command):
        yield line.strip()


# domain = 'caterpillar.com'
# for line in crtsh_curl(domain):
#     print(line)

__all__ = ['crtsh_curl']


