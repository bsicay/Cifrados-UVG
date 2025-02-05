
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# BRANDON RONALDO SICAY CUMES 21757
# MODELO UTILIZADO: GTP-o1
# CHAT UTILIZADO: https://chatgpt.com/share/67a2c876-3d5c-800f-8793-93e95de6f743


from bin_to_ascii import binary_to_ascii
from ascii_to_bin import ascii_to_bin
from xor import xor_binary
from generate_dynamic_key import generate_dynamic_key

def cipher_with_dynamic_key(text):
    """
    Cifra un texto ASCII usando una llave ASCII de la misma longitud (en caracteres).
    Retorna la tupla (texto_cifrado, llave_usada).
    """
    # Generar llave de la misma longitud en caracteres que el texto
    key = generate_dynamic_key(len(text))
    
    # Convertir ambos a binario
    text_bin = ascii_to_bin(text)
    key_bin = ascii_to_bin(key)
    # XOR
    cipher_bin = xor_binary(text_bin, key_bin)
    
    # Convertir binario a ASCII
    cipher_ascii = binary_to_ascii(cipher_bin)
    
    return cipher_ascii, key

def decipher_with_dynamic_key(cipher_text, key):
    """
    Descifra el texto cifrado usando la llave dinámica.
    """
    cipher_bin = ascii_to_bin(cipher_text)
    key_bin = ascii_to_bin(key)
    original_bin = xor_binary(cipher_bin, key_bin)
    original_text = binary_to_ascii(original_bin)
    return original_text

if __name__ == "__main__":
    mensaje = "hola"
    
    # Cifrar
    texto_cifrado, llave_usada = cipher_with_dynamic_key(mensaje)
    print(f"Texto Original : {mensaje}")
    print(f"Texto Cifrado  : {texto_cifrado}")
    print(f"Llave Usada    : {llave_usada}")
    
    # Descifrar
    texto_descifrado = decipher_with_dynamic_key(texto_cifrado, llave_usada)
    print(f"Texto Descifrado: {texto_descifrado}")
