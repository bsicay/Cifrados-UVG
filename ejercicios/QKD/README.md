# Ejercicio - Simulación del protocolo BB84 (QKD)

Implementación en Python una simulación del protocolo de Distribución de Clave Cuántica (BB84), donde:

* Alice y Bob generan y miden fotones en bases aleatorias (recta ↕ o diagonal ↗).
* Se comparan las bases por un canal público y se extraen los bits coincidentes para formar la clave secreta.
* Se analiza el efecto de un espía (Eve) interceptando fotones.

## Archivos

* `bb84_simulation.py`: Script principal que genera una tabla de 15 rondas, muestra resultados y extrae la clave.

