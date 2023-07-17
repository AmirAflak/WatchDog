#!/usr/bin/python3

import os
from typing import Generator
from configs import DOMAIN


def crtsh_curl() -> Generator[str, None, None]:
    command = f'curl -sk "https://crt.sh/?q=%.{DOMAIN}&output=json" | tr "," "\\n" | awk -F\'"\' \'/name_value/ {{gsub(/\\*\\./, "", $4); gsub(/\\\\n/,"\\n",$4);print $4}}\''
    for line in os.popen(command):
        yield line.strip()


# for line in crtsh_curl():
#     print(line)

__all__ = ['crtsh_curl']


