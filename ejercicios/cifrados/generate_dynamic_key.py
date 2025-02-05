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
