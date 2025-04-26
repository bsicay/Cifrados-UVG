# encrypt_image.py
from pathlib import Path
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from PIL import Image

BLOCK_SIZE = 16  # AES block = 16 bytes


def pad(data: bytes) -> bytes:
    """PKCS7 padding."""
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)


def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]


def encrypt_ecb(key: bytes, data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(pad(data))
    # recortamos a tamaño original (solo para visualizar)
    return enc[: len(data)]


def encrypt_cbc(key: bytes, iv: bytes, data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    enc = cipher.encrypt(pad(data))
    return enc[: len(data)]


def bytes_to_image(template_img: Image.Image, data: bytes, out_path: Path):
    """Crea y guarda una imagen a partir de los bytes cifrados."""
    img_out = Image.frombytes("L", template_img.size, data)
    img_out.save(out_path)
    print(f"Guardado {out_path}")


def main():
    # ---------- 1. Cargar imagen original ----------
    src_path = Path("example.bmp")  # o .bmp
    img = Image.open(src_path).convert("L")  # escala de grises
    pixel_bytes = img.tobytes()

    # ---------- 2. Parámetros AES ----------
    key = get_random_bytes(16)  # 128 bits
    iv = get_random_bytes(16)   # solo para CBC

    # ---------- 3. Cifrar ----------
    ecb_bytes = encrypt_ecb(key, pixel_bytes)
    cbc_bytes = encrypt_cbc(key, iv, pixel_bytes)

    # ---------- 4. Guardar resultados ----------
    bytes_to_image(img, ecb_bytes, Path("example_encrypted_ecb.png"))
    bytes_to_image(img, cbc_bytes, Path("example_encrypted_cbc.png"))

    print("Proceso terminado.")


if __name__ == "__main__":
    main()
