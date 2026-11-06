# TEST-ONLY intentionally vulnerable sink. Never import or execute.
import subprocess

def run_dns_lookup(host: str) -> str:
    command = 'nslookup ' + host
    return subprocess.check_output(command, shell=True, text=True)
