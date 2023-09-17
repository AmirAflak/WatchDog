#!/usr/bin/python3
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
apiURL= f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def new_subdomain(new_sub):
    msg = f"[+] new subdomain: {new_sub}"
    response = requests.post(apiURL, json={'chat_id': -1001612767860, 'text': msg})

def new_asset(new_ass):
    msg = f"[+] new Asset: {new_ass}"
    response = requests.post(apiURL, json={'chat_id': -1001612767860, 'text': msg})

def new_service(new_serv):
    msg = f"[+] New service: {new_serv}"
    response = requests.post(apiURL, json={'chat_id': -1001612767860, 'text': msg})

def latest_asset(latest_ass):
    msg = f"[+] Latest asset: {latest_ass}"
    response = requests.post(apiURL, json={'chat_id': -1001612767860, 'text': msg})

def Change_Service(change_serv):
    msg = f"[+] Change Service: {change_serv}"
    response = requests.post(apiURL, json={'chat_id': -1001612767860, 'text':msg})
