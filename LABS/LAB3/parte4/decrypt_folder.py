#!/usr/bin/env python3
"""
Descifra los .enc usando keyfile.json
y restaura los .txt originales.
"""
import os, json, argparse
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

BLOCK = 16

def decrypt_file(enc_path: Path, key: bytes, iv: bytes):
    data = enc_path.read_bytes()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(data[16:]), BLOCK)
    orig_name = enc_path.stem          # quita .enc
    out = enc_path.with_name(orig_name)
    out.write_bytes(pt)
    enc_path.unlink()                  # borra cifrado
    print(f"[+] {enc_path.name} → {out.name}")

def main(folder):
    folder = Path(folder).resolve()
    rec = json.loads((folder / "keyfile.json").read_text())
    key = bytes.fromhex(rec["key"])

    for f in rec["files"]:
        iv  = bytes.fromhex(f["iv"])
        enc = folder / f["file"]
        decrypt_file(enc, key, iv)

    (folder / "keyfile.json").unlink()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", help="Carpeta con los .enc y keyfile.json")
    main(ap.parse_args().folder)
