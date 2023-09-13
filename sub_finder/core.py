#!/usr/bin/python3
import os
import time
from multiprocessing import Pool
from typing import Generator
from functools import partial




def amass(target: str, use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] amass")
    if use_docker:
        amass_command = f'docker run -v OUTPUT_DIR_PATH:/.config/amass/ caffix/amass enum -passive -norecursive -noalts -d {target} 2>/dev/null'

    else:
        amass_command = f'amass enum -passive -norecursive -noalts -d {target} 2>/dev/null'

        
    for line in os.popen(amass_command):
        yield line.strip()
    
    
def findomain(target: str, use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] findomain")
    if use_docker:
        findomain_command = f'docker run -it edu4rdshl/findomain:latest -t {target} -q 2>/dev/null'
    else: 
        findomain_command = f'findomain -t {target} -q 2>/dev/null'
    for line in os.popen(findomain_command):
        yield line.strip()
        
        
def subfinder(target: str, use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] subfinder")
    if use_docker:
        subfinder_command = f"docker run projectdiscovery/subfinder:latest -d {target} -all -silent"
    else:
        subfinder_command = f"subfinder -d {target} -all -silent"  
        
    for line in os.popen(subfinder_command):
        yield line.strip()
    
        
def crtsh_curl(target: str) -> Generator[str, None, None]:
    print("[+] crtsh_curl")
    command = f'curl -sk "https://crt.sh/?q=%.{target}&output=json" | tr "," "\\n" | awk -F\'"\' \'/name_value/ {{gsub(/\\*\\./, "", $4); gsub(/\\\\n/,"\\n",$4);print $4}}\''
    for line in os.popen(command):
        yield line.strip()


def pickle_handler(f, target):
    return list(f(target))


def get_subs(target: str) -> Generator[str, None, None]:
    pool = Pool()

    seen_results = set()
    
    sub_finders = [findomain, amass, subfinder, crtsh_curl]

    for result in pool.starmap(pickle_handler, [(finder, target) for finder in sub_finders]):
        yield from (res for res in result if res not in seen_results and not seen_results.add(res))
    
    pool.close()
    pool.join()
    
if __name__ == '__main__': 
    start_time = time.time()
    with open('subs.txt', 'w') as f:
        for line in get_subs("caterpillar.com"):
            f.write(line)
            f.write("\n")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{execution_time=}")


