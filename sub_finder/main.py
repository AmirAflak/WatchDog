#!/usr/bin/python3
import os
from multiprocessing import Pool
from typing import Generator
from configs import DOMAIN


def amass(use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] amass")
    if use_docker:
        amass_command = f'docker run -v OUTPUT_DIR_PATH:/.config/amass/ caffix/amass enum -passive -norecursive -noalts -d {DOMAIN} 2>/dev/null'

    else:
        amass_command = f'amass enum -passive -norecursive -noalts -d {DOMAIN} 2>/dev/null'

        
    for line in os.popen(amass_command):
        yield line.strip()
    
    
def findomain(use_docker: bool = True) -> Generator[str, None, None]:
    print("[+] findomain")
    if use_docker:
        findomain_command = f'docker run -it edu4rdshl/findomain:latest -t {DOMAIN} -q 2>/dev/null'
    else: 
        findomain_command = f'findomain -t {DOMAIN} -q 2>/dev/null'
    for line in os.popen(findomain_command):
        yield line.strip()
        
        
def subfinder(use_docker: bool = True) -> Generator[str, None, None]:
    if use_docker:
        subfinder_command = f"docker run projectdiscovery/subfinder:latest -d {DOMAIN} -all"
    else:
        subfinder_command = f"subfinder -d {DOMAIN} -all"  
        
    for line in os.popen(subfinder_command):
        yield line.strip()
    
        
def crtsh_curl() -> Generator[str, None, None]:
    command = f'curl -sk "https://crt.sh/?q=%.{DOMAIN}&output=json" | tr "," "\\n" | awk -F\'"\' \'/name_value/ {{gsub(/\\*\\./, "", $4); gsub(/\\\\n/,"\\n",$4);print $4}}\''
    for line in os.popen(command):
        yield line.strip()


def get_subs() -> Generator[str, None, None]:
    pool = Pool()

    seen_results = set()
    
    sub_finders = [findomain, amass, subfinder, crtsh_curl]
    
    # for result in pool.imap(lambda f: list(f()), sub_finders):
    for result in pool.imap(pickle_handler, sub_finders):
        yield from (res for res in result if res not in seen_results and not seen_results.add(res))
    
    pool.close()
    pool.join()
    
def pickle_handler(f):
    return list(f())
    

if __name__ == '__main__': 
    for line in get_subs():
        print(line)
