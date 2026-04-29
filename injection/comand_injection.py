import os

def ping(host):
    os.system(f"ping -c 1 {host}")