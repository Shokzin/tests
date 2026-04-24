import subprocess

def run_command(cmd):
    # ❌ Vulnerável
    subprocess.run(cmd, shell=True)