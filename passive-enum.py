#!/usr/bin/python3

import sys
import os

#getting the target domain
domain = sys.argv[1]

#making the target directory
def mkdir():
    print(f'[+] making the {domain} directory ...')
    mkdir_command = f'mkdir {domain}'
    os.system(mkdir_command)

#sub enumeration via subfinder
def subfinder():
    print("[+] subfinder")
    subfinder_command = f"subfinder -d {domain} -all | anew {domain}/subfinder.subs"
    os.system(subfinder_command)

#sub enumeration via findomain
def findomain():
    print("[+] findomain")
    findomain_command = f'findomain -t {domain} -q 2>/dev/null | anew {domain}/findomain.subs'
    os.system(findomain_command)

#sub enumeration via assetfinder
def assetfinder():
    print("[+] assetfinder")
    assetfinder_command = f'assetfinder --subs-only {domain} | anew {domain}/assetfinder.subs'
    os.system(assetfinder_command)

#sub enumeration via amass
def amass():
    print("[+] amass")
    amass_command = f'amass enum -passive -norecursive -noalts -d {domain} 2>/dev/null | anew {domain}/amass.subs'
    os.system(amass_command)
    
#sub enumeration via crtsh(curl)
default_command = """curl -sk "https://crt.sh/?q=%.{0}&output=json" | tr ',' '\\n' | awk -F'"' '/name_value/ {{gsub(/\*\./, "", $4); gsub(/\\\\n/,"\\n",$4);print $4}}' | anew {0}/crtsh_curl.subs"""

def command_maker():
    global curl_crtsh_command
    curl_crtsh_command = default_command.format(domain)

command_maker()

def curl_crtsh():
    print("[+] curl crtsh")
    os.system(curl_crtsh_command)

#sub enumeration via crtsh
#first add the crtsh function from the requirement_functions file
def crtsh():
    crtsh_command = f"crtsh {domain} | anew {domain}.subs"
    os.system(crtsh_command)

def run_all():
    subfinder()
    findomain()
    assetfinder()
    amass()
    curl_crtsh()

run_all()
