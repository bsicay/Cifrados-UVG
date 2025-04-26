"""
Universidad del Valle de Guatemala

Programa para descifrar un texto cifrado con desplazamiento mediante fuerza bruta y análisis
de frecuencias.

Autor: Diego Morales Aquino - 21762
Código basado en el laboratorio 1B
"""
import numpy as np
from scipy.spatial.distance import jensenshannon


# Frecuencia de letras en español (aproximación)
sp_frequencies = {
    "a": 0.11525, "b": 0.02215, "c": 0.04019, "d": 0.05010, "e": 0.12181,
    "f": 0.00692, "g": 0.01768, "h": 0.00703, "i": 0.06247, "j": 0.00493,
    "k": 0.00011, "l": 0.04967, "m": 0.03157, "n": 0.06712, "o": 0.08683,
    "p": 0.02510, "q": 0.00877, "r": 0.06871, "s": 0.07977, "t": 0.04632,
    "u": 0.02927, "v": 0.01138, "w": 0.00017, "x": 0.00215, "y": 0.01008,
    "z": 0.00467, "á": 0.00502, "é": 0.00433, "í": 0.00725, "ñ": 0.00311,
    "ó": 0.00827, "ú": 0.00168, "ü": 0.00012
}

# Limitar caracteres alfabéticos
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_decypher(text, shift):
    """Descifrar el texto con un desplazamiento (cifrado César)"""
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char  # Ignorar chars que no están en el alfabeto
    return decrypted_text

def get_text_probability_distr(text):
    """Calcular la distribución de probabilidad de letras en un texto"""
    text = text.lower()
    total_chars = len(text)
    probability = {char: 0 for char in sp_frequencies}  # Iniciar distribución en cero

    for char in text:
        if char in probability:
            probability[char] += 1

    for char in probability:
        probability[char] /= total_chars if total_chars > 0 else 1 # Evitar división por cero
    return probability

def normalize_distribution(dist):
    total = sum(dist.values())
    if total == 0:
        return {k: 0 for k in dist}
    return {k: v / total for k, v in dist.items()}

def eval_distr(dist):
    """Calcula la distancia de Jensen-Shannon entre una distribución y la distribución teórica."""
    dist = normalize_distribution(dist)
    dist_theo = normalize_distribution(sp_frequencies)

    # Verificar si alguna de las distribuciones es completamente nula
    if sum(dist.values()) == 0 or sum(dist_theo.values()) == 0:
        return float('inf')  # Si alguna distribución es vacía, asignar una métrica infinita

    keys = set(dist.keys()).union(dist_theo.keys())
    p = np.array([dist.get(k, 0) for k in keys])
    q = np.array([dist_theo.get(k, 0) for k in keys])

    return jensenshannon(p, q)  # Distancia de JS (0 = idénticas, >0 = diferentes)

def caesar_bruteforce(text):
    """Descifra un texto cifrado con el cifrado César con un desplazamiento dado."""
       
    results = []
    # Ir probando que cada letra sea la más probable en español
    for shift in range(len(alphabet)):
        decyphered_text = caesar_decypher(text, shift)
        decypher_prob_distr = get_text_probability_distr(decyphered_text)
        # calcular metrica
        metric = eval_distr(decypher_prob_distr)
        
        results.append((shift, metric, decyphered_text))

    return sorted(results, key=lambda x: x[1], reverse=False)


if __name__ == "__main__":
    cipher_text = "SV OHU JVUZLNBPKV, OHU LUJVUAYHKV BUH MSHN WHYH LS ZPNBPLUAL KLZHMPV MSHN{JYFWAV_HUHSFZPZ}"

    results = caesar_bruteforce(cipher_text)

    for shift, metric, decyphered_text in results:
        print(f"Shift: {shift}, Métrica: {metric}, Texto descifrado: {decyphered_text}")
