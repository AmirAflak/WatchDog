#!/usr/bin/python3

import os
import sys
from typing import Generator
import time

def amass(domain: str, use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] amass")
    if use_docker:
        amass_command = f'docker run -v OUTPUT_DIR_PATH:/.config/amass/ caffix/amass enum -passive -norecursive -noalts -d {domain} 2>/dev/null'

    else:
        amass_command = f'amass enum -passive -norecursive -noalts -d {domain} 2>/dev/null'

        
    for line in os.popen(amass_command):
        yield line.strip()
        
       
domain = 'caterpillar.com'
amass(domain)


# TODO: benchmark execution with and without docker using below sample

# start_time = time.time()
# for url in amass(domain):
#     continue
# end_time = time.time()
# execution_time = end_time - start_time
# print(f'execution time with yield: {execution_time}')






