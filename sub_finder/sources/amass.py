#!/usr/bin/python3

import os
from typing import Generator
from configs import DOMAIN
import time

def amass(use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] amass")
    if use_docker:
        amass_command = f'docker run -v OUTPUT_DIR_PATH:/.config/amass/ caffix/amass enum -passive -norecursive -noalts -d {DOMAIN} 2>/dev/null'

    else:
        amass_command = f'amass enum -passive -norecursive -noalts -d {DOMAIN} 2>/dev/null'

        
    for line in os.popen(amass_command):
        yield line.strip()
        
       

# for line in amass():
#     print(line)


# TODO: benchmark execution with and without docker using below sample

# start_time = time.time()
# for url in amass(use_docker=True):
#     continue
# end_time = time.time()
# execution_time = end_time - start_time
# print(f'execution time with docker: {execution_time}')

# start_time = time.time()
# for url in amass(use_docker=False):
#     continue
# end_time = time.time()
# execution_time = end_time - start_time
# print(f'execution time without docker: {execution_time}')


__all__ = ['amass']



