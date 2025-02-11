
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# BRANDON RONALDO SICAY CUMES 21757
# MODELO UTILIZADO: GTP-o1
# CHAT UTILIZADO: https://chatgpt.com/share/67a2c876-3d5c-800f-8793-93e95de6f743


def base64_to_ascii(b64_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Contar cuántos '=' hay al final
    padding_count = b64_string.count('=')
    
    # Quitar los '=' del string antes de procesar
    b64_string = b64_string.replace('=', '')
    
    # Convertir cada carácter base64 en sus 6 bits correspondientes
    bit_string = ""
    for ch in b64_string:
        val_6_bits = base64_chars.index(ch)  # índice entre 0 y 63
        bit_string += f"{val_6_bits:06b}"    # 6 bits por carácter base64
    
    bits_to_remove = 2 * padding_count
    if bits_to_remove > 0:
        bit_string = bit_string[:-bits_to_remove]
    
    # Convertir los bits restantes en caracteres ASCII (en grupos de 8 bits)
    ascii_text = ""
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        if len(byte) < 8:
            break
        ascii_text += chr(int(byte, 2))
    
    return ascii_text

