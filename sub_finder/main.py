#!/usr/bin/python3
import os
from multiprocessing import Pool
from typing import Generator
from sources.findomain import *
from sources.crtsh import *
from sources.amass import *
from sources.subfinder import *
from sources.assetfinder import *
from sources.crtsh_curl import *

def main() -> Generator[str, None, None]:
    pool = Pool()

    seen_results = set()
    
    sub_finders = [findomain, crtsh, amass, subfinder, assetfinder, crtsh_curl]
    
    for result in pool.imap(lambda f: list(f()), sub_finders):
        yield from (res for res in result if res not in seen_results and not seen_results.add(res))
    
    pool.close()
    pool.join()
    


for line in main():
    print(line)
