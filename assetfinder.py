#!/usr/bin/python3
import os
from typing import Generator
from configs import DOMAIN


def assetfinder() -> Generator[str, None, None]:
    print("[+] assetfinder")
    assetfinder_command = f'assetfinder --subs-only {DOMAIN}'
    
    for line in os.popen(amass_command):
        yield line.strip()

# for line in assetfinder():
#     print(line)

__all__ = ['assetfinder']