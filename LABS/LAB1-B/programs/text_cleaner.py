import re
import unicodedata

def text_cleaner(texto):
    """
    Elimina acentos y caracteres no alfabéticos de la cadena de texto.
    Convierte también todo a minúsculas.

    """
    # 1. Convertir a minúsculas
    texto = texto.lower()
    
    # 2. Normalizar (NFD) para separar diacríticos (tildes, etc.)
    texto_nfd = unicodedata.normalize('NFD', texto)
    
    # 3. Eliminar diacríticos (caracteres "combining")
    #    Filtramos todos los caracteres que no estén clasificados como "combining"
    texto_sin_tildes = ''.join(char for char in texto_nfd if not unicodedata.combining(char))
    
    # 4. Remover todos los caracteres que no sean letras a-z
    texto_limpio = re.sub(r'[^a-z]+', '', texto_sin_tildes)
    
    return texto_limpio

if __name__ == "__main__":
    ejemplo = "Hola, ¿cómo estás?"
    resultado = text_cleaner(ejemplo)
    print("Texto original:", ejemplo)
    print("Texto limpio  :", resultado)


