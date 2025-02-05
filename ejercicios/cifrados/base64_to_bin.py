
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# BRANDON RONALDO SICAY CUMES 21757
# MODELO UTILIZADO: GTP-o1
# CHAT UTILIZADO: https://chatgpt.com/share/67a2c876-3d5c-800f-8793-93e95de6f743


def base64_to_binary(b64_string):
    """
    Decodifica una cadena en Base64 y devuelve su contenido en binario (bits) como una cadena.
    Procesa manualmente los caracteres, sin utilizar librerías.
    """
    
    # Tabla de caracteres Base64 estándar y su índice (0..63)
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Contar cuántos '=' hay (padding)
    padding_count = b64_string.count('=')
    
    # Eliminar los '=' para poder mapear los caracteres a bits
    b64_string = b64_string.replace('=', '')
    
    # 1) Convertir cada carácter Base64 en 6 bits
    bit_string = ""
    for ch in b64_string:
        # Obtener el índice (valor entre 0..63)
        val_6_bits = base64_chars.index(ch)
        # Convertirlo a binario de 6 bits y concatenar
        bit_string += f"{val_6_bits:06b}"

    return bit_string

# Ejemplo de uso
if __name__ == "__main__":
    entrada_base64 = "aG9sYQ=="  # "hola"
    resultado_binario = base64_to_binary(entrada_base64)
    print(f"Base64: {entrada_base64}")
    print(f"Binario (bits): {resultado_binario}")
    
    # Para verificar: si decodificamos "hola" a ASCII:
    #   'h' = 01101000
    #   'o' = 01101111
    #   'l' = 01101100
    #   'a' = 01100001
    # Concatenado: 01101000011011110110110001100001
    # Debe coincidir con 'resultado_binario'.
