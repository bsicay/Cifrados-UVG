import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pathlib import Path

# root folder (folder to encrypt as example)
encryption_folder = "./test_folder"

def generate_key():
    key = get_random_bytes(32)  # 256 bits
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    # generate random iv
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # read file
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # apply padding PKCS7
    padding_length = 16 - (len(file_data) % 16)
    padded_data = file_data + bytes([padding_length] * padding_length)
    
    # encrypt data
    encrypted_data = cipher.encrypt(padded_data)
    
    # save iv and encrypted data
    with open(file_path, "wb") as file:
        file.write(iv + encrypted_data)

def encrypt_folder():
    # generate new encryption key
    key = generate_key()
    
    # iterate over all files in the directory
    for path in Path(encryption_folder).rglob("*"):
        if path.is_file():
            try:
                print(f"Encrypting: {path}")
                encrypt_file(str(path), key)
            except Exception as e:
                print(f"Error encrypting {path}: {str(e)}")

if __name__ == "__main__":
    if not os.path.exists(encryption_folder):
        print(f" {encryption_folder} does not exist")
        exit(0)
    
    # execute encryption
    encrypt_folder()
    print("Files encrypted!")