
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# BRANDON RONALDO SICAY CUMES 21757
# MODELO UTILIZADO: GTP-o1
# CHAT UTILIZADO: https://chatgpt.com/share/67a2c876-3d5c-800f-8793-93e95de6f743


def ascii_to_bin(texto):
    """
    Convierte una cadena en ASCII a una cadena de bits (binario).
    Cada carácter se convierte en su representación de 8 bits.
    """
    binario = ''.join(format(ord(c), '08b') for c in texto)
    return binario


def bin_to_base64(binary_str):

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Ajustar la longitud del binario a múltiplo de 6 (padding con '0' si sobra)
    length = len(binary_str)
    remainder = length % 6
    
    if remainder != 0:
        padding_bits = 6 - remainder
        binary_str += '0' * padding_bits
    else:
        padding_bits = 0
    
    # Dividir en grupos de 6 bits
    base64_encoded = []
    for i in range(0, len(binary_str), 6):
        chunk_6 = binary_str[i:i+6]
        decimal_val = int(chunk_6, 2)
        base64_encoded.append(base64_chars[decimal_val])
    
    # Asegurar que la salida sea múltiplo de 4 caracteres, añadiendo '='
    
    encoded_str = ''.join(base64_encoded)
    base64_len = len(encoded_str) % 4
    
    if base64_len != 0:
        # número de '=' necesario para completar un múltiplo de 4
        encoded_str += '=' * (4 - base64_len)
    
    return encoded_str



def ascii_to_base64(texto):
    """
    Convierte una cadena en ASCII a una cadena de bits (binario).
    Cada carácter se convierte en su representación de 8 bits.
    """
    binary = ascii_to_bin(texto)
    base64 = bin_to_base64(binary)
    return base64
