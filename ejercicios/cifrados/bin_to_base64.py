
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# BRANDON RONALDO SICAY CUMES 21757
# MODELO UTILIZADO: GTP-o1
# CHAT UTILIZADO: https://chatgpt.com/share/67a2c876-3d5c-800f-8793-93e95de6f743


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

if __name__ == "__main__":
    bin_hola = "01101000011011110110110001100001"
    
    resultado = bin_to_base64(bin_hola)
    print("Binario  :", bin_hola)
    print("Base64   :", resultado)
    # "SG9sYQ=="
