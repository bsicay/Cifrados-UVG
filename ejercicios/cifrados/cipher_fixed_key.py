from bin_to_ascii import binary_to_ascii
from ascii_to_bin import ascii_to_bin
from xor import xor_binary

def ascii_to_bin_key(key, length):
    """
    Convierte la llave ASCII a binario y la repite o trunca para igualar 'length' bits.
    Asume que 'length' es múltiplo de 8.
    """
    # Convierte la llave completa a binario
    key_bin_full = ''.join(format(ord(c), '08b') for c in key)
    
    # Repite la llave hasta alcanzar 'length' bits (o la trunca si es más larga)
    repeated_key = (key_bin_full * ((length // len(key_bin_full)) + 1))[:length]
    return repeated_key

def cipher_with_fixed_key(text, key):
    """
    Cifra un texto ASCII usando una llave ASCII de tamaño fijo.
    """
    text_bin = ascii_to_bin(text)
    
    text_len = len(text_bin)
    
    # 3. Ajustar llave binaria a la longitud del texto
    key_bin = ascii_to_bin_key(key, text_len)
    cipher_bin = xor_binary(text_bin, key_bin)
    
    cipher_ascii = binary_to_ascii(cipher_bin)
    return cipher_ascii

if __name__ == "__main__":
    texto_original = "hola"
    llave_fija = "ABC"  # Llave ASCII de tamaño fijo 
    
    cifrado = cipher_with_fixed_key(texto_original, llave_fija)
    print(f"Texto Original : {texto_original}")
    print(f"Texto Cifrado  : {cifrado}")
    
    # Descifrado (se usa la misma función con la misma llave, ya que XOR es reversible)
    descifrado = cipher_with_fixed_key(cifrado, llave_fija)
    print(f"Texto Descifrado: {descifrado}")
