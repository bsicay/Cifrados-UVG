
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

if __name__ == "__main__":
    mensaje = input('Enter ASCII message\n') 
    resultado = ascii_to_bin(mensaje)
    print(f"Texto ASCII  : {mensaje}")
    print(f"Binario      : {resultado}")
 