
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

def xor_ascii(text1, text2):
    """
    Aplica la operación XOR entre dos cadenas binarias de la misma longitud.
    Retorna una nueva cadena binaria resultado de binario1 XOR binario2.
    """
    binario1 = ascii_to_bin(text1)
    binario2 = ascii_to_bin(text2)

    if len(binario1) != len(binario2):
        length = max(len(binario1), len(binario2))
        binario1 = binario1.zfill(length)
        binario2 = binario2.zfill(length)
    
    resultado = []
    for b1, b2 in zip(binario1, binario2):
        # XOR bit a bit
        xor_bit = str(int(b1) ^ int(b2))
        resultado.append(xor_bit)
    
    return ''.join(resultado)


def xor_binary(binario1, binario2):
    """
    Aplica la operación XOR entre dos cadenas binarias de la misma longitud.
    Retorna una nueva cadena binaria resultado de binario1 XOR binario2.
    """
    bin1 = binario1
    bin2 = binario2
    if len(binario1) != len(binario2):
        length = max(len(binario1), len(binario2))
        bin1 = bin1.zfill(length)
        bin2 = bin2.zfill(length)
    
    
    resultado = []
    for b1, b2 in zip(bin1, bin2):
        # XOR bit a bit
        xor_bit = str(int(b1) ^ int(b2))
        resultado.append(xor_bit)
    
    return ''.join(resultado)

def xor_binaries(text_bin, key_bin):
    """
    Aplica XOR bit a bit entre dos cadenas binarias.
    Si key_bin es menor que text_bin, se repite hasta igualar la longitud.
    
    Args:
        text_bin (str): Cadena binaria que representa el texto.
        key_bin (str): Cadena binaria que representa la llave.
        
    Returns:
        str: Resultado del XOR en forma de cadena binaria.
    """
    # Repetir la llave hasta alcanzar la longitud del texto
    if len(key_bin) < len(text_bin):
        repetitions = (len(text_bin) // len(key_bin)) + 1
        key_bin = (key_bin * repetitions)[:len(text_bin)]
    else:
        key_bin = key_bin[:len(text_bin)]
    
    # Aplicar XOR bit a bit
    resultado = []
    for bit_text, bit_key in zip(text_bin, key_bin):
        resultado.append(str(int(bit_text) ^ int(bit_key)))
    
    return ''.join(resultado)
