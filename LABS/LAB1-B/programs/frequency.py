

from programs.text_cleaner import text_cleaner

# Prompt GPT-4o: Haz una función que realice un análisis de frecuencia de un texto plano, con un alfabeto 'abcdefghijklmnñopqrstuvwxyz'
# se espera que su función calcule las probabilidades (las frecuencias divido el total de caracteres).

def calcular_distribucion(texto):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    frecuencias = {letra: 0 for letra in alfabeto}
    text = text_cleaner(texto)

    for char in text:
        if char in alfabeto:
            frecuencias[char] += 1

    total_caracteres = sum(frecuencias.values())

    probabilidades = {letra: (frecuencia / total_caracteres) * 100  for letra, frecuencia in frecuencias.items()}

    return probabilidades


# Prompt GPT-4o: Haz una función que grafique las frecuencias  en un texto en comparación a estas frecuencias teóricas.
import matplotlib.pyplot as plt

def crear_histograma(distribuciones):

    sp_frequencies = {
    "a": 0.11525,
    "b": 0.02215,
    "c": 0.04019,
    "d": 0.05010,
    "e": 0.12181,
    "f": 0.00692,
    "g": 0.01768,
    "h": 0.00703,
    "i": 0.06247,
    "j": 0.00493,
    "k": 0.00011,
    "l": 0.04967,
    "m": 0.03157,
    "n": 0.06712,
    "o": 0.08683,
    "p": 0.02510,
    "q": 0.00877,
    "r": 0.06871,
    "s": 0.07977,
    "t": 0.04632,
    "u": 0.02927,
    "v": 0.01138,
    "w": 0.00017,
    "x": 0.00215,
    "y": 0.01008,
    "z": 0.00467,
    "á": 0.00502,
    "é": 0.00433,
    "í": 0.00725,
    "ñ": 0.00311,
    "ó": 0.00827,
    "ú": 0.00168,
    "ü": 0.00012
    }

    etiquetas = probabilidad_real.keys()
    valores_reales = [probabilidad_real[letra] for letra in etiquetas]
    valores_calculados = [distribuciones.get(letra, 0) for letra in etiquetas]
    

    x = range(len(etiquetas))
    ancho = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, valores_reales, ancho, label='Frecuencias Reales')
    rects2 = ax.bar([p + ancho for p in x], valores_calculados, ancho, label='Frecuencias Calculadas')

    ax.set_ylabel('Frecuencias')
    ax.set_title('Comparación de Frecuencias Reales y Calculadas por Letra')
    ax.set_xticks([p + ancho / 2 for p in x])
    ax.set_xticklabels(etiquetas)
    ax.legend()

    plt.show()
