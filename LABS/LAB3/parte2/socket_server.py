# socket_server.py
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST = "0.0.0.0"   # Escucha en todas las interfaces
PORT = 8080
KEY  = b"0123456789abcdef"   # 16 bytes (AES-128)

def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((HOST, PORT))
    srv.listen(1)
    print(f"[+] Escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = srv.accept()
        print(f"[+] Conexión de {addr}")
        try:
            while True:
                # 16 bytes de IV + resto = ciphertext
                data = conn.recv(4096)
                if not data:
                    break

                iv  = data[:16]
                ct  = data[16:]

                # (Opcional) descifrar en el servidor
                cipher = AES.new(KEY, AES.MODE_CBC, iv)
                try:
                    plaintext = unpad(cipher.decrypt(ct), AES.block_size)
                    print(f"[+] Mensaje: {plaintext.decode(errors='ignore')}")
                except ValueError:
                    print("[!] Padding incorrecto (dato corrupto)")

        finally:
            conn.close()
            print("[*] Conexión cerrada")

if __name__ == "__main__":
    main()
