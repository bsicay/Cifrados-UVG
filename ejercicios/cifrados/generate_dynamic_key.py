
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# BRANDON RONALDO SICAY CUMES 21757
# MODELO UTILIZADO: GTP-o1
# CHAT UTILIZADO: https://chatgpt.com/share/67a2c876-3d5c-800f-8793-93e95de6f743


import random
import string

def generate_dynamic_key(length=16):
    """
    Genera una llave alfanumérica (ASCII) de longitud 'length'.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(caracteres) for _ in range(length))
    return key

if __name__ == "__main__":
    # Genera una llave de longitud 10, por ejemplo
    llave = generate_dynamic_key(10)
    print(f"Llave generada (10 caracteres): {llave}")
