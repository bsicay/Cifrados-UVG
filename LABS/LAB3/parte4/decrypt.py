import os
from Crypto.Cipher import AES
from pathlib import Path

# root folder (folder to decrypt as example)
encryption_folder = "./test_folder"

def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        # read iv (first 16 bytes) and encrypted data
        iv = file.read(16)
        encrypted_data = file.read()
    
    # create cipher object with key and iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # remove padding PKCS7
    padding_length = decrypted_data[-1]
    unpadded_data = decrypted_data[:-padding_length]
    
    # save decrypted data
    with open(file_path, "wb") as file:
        file.write(unpadded_data)

def decrypt_folder():
    try:
        # load encryption key
        key = load_key()
        
        # iterate over all files in the directory
        for path in Path(encryption_folder).rglob("*"):
            if path.is_file():
                try:
                    print(f"Decrypting: {path}")
                    decrypt_file(str(path), key)
                except Exception as e:
                    print(f"Error decrypting {path}: {str(e)}")
        
        print("Decryption completed successfully")
        return True
    
    except FileNotFoundError:
        print("Error: Key file not found")
        return False
    except Exception as e:
        print(f"Error during decryption: {str(e)}")
        return False

if __name__ == "__main__":
    # check if the directory exists
    if not os.path.exists(encryption_folder):
        print(f"{encryption_folder} does not exist")
        exit(1)
    
    # execute decryption
    decrypt_folder()