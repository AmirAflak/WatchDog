#!/usr/bin/python3
import os
from typing import Generator

def assetfinder(domain: str) -> Generator[str, None, None]:
    print("[+] assetfinder")
    assetfinder_command = f'assetfinder --subs-only {domain}'
    
    for line in os.popen(amass_command):
        yield line.strip()

# domain = 'caterpillar.com'
# for line in assetfinder(domain):
#     print(line)

__all__ = ['assetfinder']