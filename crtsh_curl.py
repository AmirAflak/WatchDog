#!/usr/bin/python3

import os
import sys

domain = sys.argv[1]

default_command = """curl -sk "https://crt.sh/?q=%.{0}&output=json" | tr ',' '\\n' | awk -F'"' '/name_value/ {{gsub(/\*\./, "", $4); gsub(/\\\\n/,"\\n",$4);print $4}}' | anew crtsh_curl.subs"""

def command_maker():
    global curl_crtsh_command
    curl_crtsh_command = default_command.format(domain)

command_maker()

def curl_crtsh():
    os.system(curl_crtsh_command)

curl_crtsh()
