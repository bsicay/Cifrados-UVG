

from text_cleaner import text_cleaner

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

    probabilidad_real = {
        "a": 12.53, "b": 1.42, "c": 4.68, "d": 5.86, "e": 13.68, "f": 0.69, "g": 1.01, "h": 0.70, "i": 6.25,
        "j": 0.44, "k": 0.02, "l": 4.97, "m": 3.15, "n": 6.71, "ñ": 0.31, "o": 8.68, "p": 2.51, "q": 0.88,
        "r": 6.87, "s": 7.98, "t": 4.63, "u": 3.93, "v": 0.90, "w": 0.01, "x": 0.22, "y": 0.90, "z": 0.52, "ñ": 0
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
