import streamlit as st
import subprocess
import socket

st.set_page_config(page_title="LAN Client Tracker", layout="wide")
st.title("📡 Office Network - Client PC Status")

client_list = {
    "HR-PC": "192.168.1.54",
    "Finance-PC": "192.168.1.195",
    "Marketing-PC": "192.168.1.193",
    "Dev-Server": "192.168.1.150"
    # Add more as needed
}

def ping_device(ip):
    try:
        result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        return "🟢 Online" if "TTL=" in result.stdout else "🔴 Offline"
    except:
        return "❌ Error"

for name, ip in client_list.items():
    status = ping_device(ip)
    st.write(f"**{name}** ({ip}): {status}")
