import socket
from cryptography.fernet import Fernet

# Generate key (RUN ONCE and copy to client)
key = Fernet.generate_key()
print("🔑 SHARE THIS KEY WITH CLIENT:")
print(key.decode())

cipher = Fernet(key)

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("\n🚀 Server listening on port 5000...")

conn, addr = server.accept()
print(f"✅ Connected from: {addr}")

while True:
    try:
        data = conn.recv(4096)
        if not data:
            break

        decrypted = cipher.decrypt(data)
        print(f"📩 Received (Decrypted): {decrypted.decode()}")

    except Exception as e:
        print("⚠️ Error:", e)
        break

conn.close()
print("🔌 Connection closed")