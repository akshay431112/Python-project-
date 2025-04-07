import psutil
import time
import os

def show_stats():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🎛️ System Mini Dashboard\n")
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
        print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
        time.sleep(3)

show_stats()
