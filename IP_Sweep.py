import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# Change this to match your subnet
network = ipaddress.ip_network("192.168.1.0/24", strict=False)

def ping(ip):
    result = subprocess.run(["ping", "-n", "1", "-w", "200", str(ip)], capture_output=True, text=True)
    if "TTL=" in result.stdout:
        return str(ip)
    return None

print("Scanning your LAN...")
live_hosts = []

with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(ping, network.hosts())

for ip in results:
    if ip:
        live_hosts.append(ip)

print("🟢 Active Devices:")
for ip in live_hosts:
    print(ip)
