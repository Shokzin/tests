import os

def ping(host):
    # ❌ Vulnerável
    os.system(f"ping -c 1 {host}")