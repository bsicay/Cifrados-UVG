# socket_client.py
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

SERVER_IP   = "192.168.0.2"     # ⇦ IP de la PC que ejecuta el servidor
PORT        = 8080
KEY         = b"0123456789abcdef"  # Debe ser la MISMA clave

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER_IP, PORT))
        print(f"[+] Conectado a {SERVER_IP}:{PORT}")

        while True:
            msg = input("Mensaje (exit para salir): ")
            if msg.lower() == "exit":
                break

            iv = os.urandom(16)
            cipher = AES.new(KEY, AES.MODE_CBC, iv)
            ct = cipher.encrypt(pad(msg.encode(), AES.block_size))

            sock.sendall(iv + ct)  # IV ⧺ ciphertext

if __name__ == "__main__":
    main()
