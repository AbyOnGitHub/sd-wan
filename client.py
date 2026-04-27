import subprocess
import time
import re
import socket
from cryptography.fernet import Fernet

WIFI = "Wi-Fi"
ETH = "Ethernet"
TARGET = "8.8.8.8"

SERVER_IP = "127.0.0.1"   # change if needed
PORT = 5000

# Paste key from server here
KEY = b'your_generated_key_here'
cipher = Fernet(KEY)

def ping():
    try:
        out = subprocess.check_output(f"ping -n 4 {TARGET}", shell=True, text=True)
        lat = int(re.search(r"Average = (\d+)ms", out).group(1))
        loss = int(re.search(r"\((\d+)% loss\)", out).group(1))
        return lat, loss
    except:
        return 999, 100

def set_priority(primary):
    if primary == "wifi":
        subprocess.run(f'netsh interface ipv4 set interface "{WIFI}" metric=10', shell=True)
        subprocess.run(f'netsh interface ipv4 set interface "{ETH}" metric=50', shell=True)
    else:
        subprocess.run(f'netsh interface ipv4 set interface "{ETH}" metric=10', shell=True)
        subprocess.run(f'netsh interface ipv4 set interface "{WIFI}" metric=50', shell=True)

def connect_server():
    while True:
        try:
            s = socket.socket()
            s.connect((SERVER_IP, PORT))
            print("Connected to server")
            return s
        except:
            print("Retrying connection...")
            time.sleep(3)

sock = connect_server()

while True:
    print("\nChecking network...")

    # Test WiFi
    set_priority("wifi")
    time.sleep(2)
    lat1, loss1 = ping()
    score1 = lat1 + loss1 * 5

    # Test Ethernet
    set_priority("eth")
    time.sleep(2)
    lat2, loss2 = ping()
    score2 = lat2 + loss2 * 5

    print(f"WiFi Score: {score1}")
    print(f"Ethernet Score: {score2}")

    if score1 < score2:
        best = "wifi"
    else:
        best = "eth"

    print(f"Best Path: {best}")
    set_priority(best)

    # Send encrypted message
    try:
        message = f"Data via {best} | WiFi:{score1} ETH:{score2}"
        encrypted = cipher.encrypt(message.encode())
        sock.send(encrypted)
        print("Encrypted data sent")
    except:
        print("Connection lost. Reconnecting...")
        sock = connect_server()

    time.sleep(5)
