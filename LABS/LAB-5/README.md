# Criptografía Cuántica (BB84) – Laboratorio e Interfaz Web

## Descripción del Laboratorio

En este laboratorio exploramos el protocolo BB84 de Distribución de Clave Cuántica (QKD) de manera práctica. Los objetivos fueron:

-   **Entender BB84:** Comprender la mecánica de “lanzar moneda” para elegir bases (↕ o ↗) y cómo Alice y Bob construyen una clave secreta segura.
    
-   **Simular QKD con código:** Implementar en Python una simulación paso a paso que ilustre la generación de bits de Alice, las bases de Alice y Bob, las mediciones de Bob, y (opcionalmente) el ataque de Eve.
    
-   **Ver el rol del azar:** Mostrar que, cuando las bases coinciden, el bit realmente sirve para la clave; cuando no, se descarta. Si Eve intercepta con base equivocada, se introducen errores que Alice y Bob pueden detectar.
    
-   **Traducir lo cuántico a algo entendible:** Generar tablas y una explicación breve que alguien sin conocimientos profundos de física pueda seguir.
    
-   **Visualizar impacto futuro:** Concluir cómo la criptografía cuántica diferirá de los cifrados tradicionales basados en problemas computacionales.
    

## Estructura del Repositorio

```
├── bb84_simulation.py       # Simulación en Python del protocolo BB84
├── index.html               # Página web interactiva para “lanzar monedas” y construir la clave
└── README.md                # Este archivo

```

----------

## 1. Simulación en Python (`bb84_simulation.py`)

### Objetivos de la Simulación

1.  Generar **n** bits aleatorios de Alice.
    
2.  Generar bases aleatorias para Alice (↕ o ↗) lanzando “moneda virtual”.
    
3.  Generar bases aleatorias para Bob (↕ o ↗) lanzando otra moneda.
    
4.  Simular el bit que Bob obtiene:
    
    -   Si su base coincide con la base de origen (Alice si no hay Eve, o Eve si intercepta), Bob lee el mismo bit.
        
    -   Si no coincide, Bob recibe un bit aleatorio.
        
5.  Comparar las bases de Alice y Bob en un canal público (sin revelar bits) y formar la clave secreta con los bits donde las bases coincidieron.
    
6.  Opcionalmente incluir a **Eve**, que intercepta y mide en una base elegida al azar, reenvía un bit (correcto o aleatorio) a Bob, generando errores detectables.
    

### Cómo funciona el script

-   Se define `simulate_bb84(n_bits, include_eve)`:
    
    1.  **Alice** lanza moneda (`flipCoin`) → obtiene `0` o `1` → base `↕` (recta) si `0`, `↗` (diagonal) si `1`.
        
    2.  Si `include_eve = true`, **Eve** lanza moneda → base propia → mide el bit de Alice; si base equivocada, obtiene bit aleatorio.
        
    3.  **Bob** lanza moneda → elige su base y mide el fotón que llegó (de Alice o de Eve).
        
    4.  Se registra en una tabla cada ronda:
        
        -   N° de ronda
            
        -   Bit y base de Alice, “moneda” de Alice
            
        -   Base y bit medido por Eve (si está activa), “moneda” de Eve
            
        -   Base y bit de Bob, “moneda” de Bob
            
        -   “Bases coinciden” (sí/no)
            
        -   “Usar?” (sí/no) → si `Bases coinciden = sí`, ese bit se añade a la clave.
            
-   Al terminar las `n` rondas (por defecto 15), se muestra:
    
    -   Todas las filas de la tabla en consola.
        
    -   La clave secreta generada (los bits donde “Usar? = sí”).
        
    -   Cantidad de bits finales vs total (y porcentaje).
        

### Ejecución

1.  Asegúrate de tener Python 3 instalado.
    
2.  Ejecuta:
    
    ```bash
    python bb84_simulation.py
    
    ```
    
3.  Verás en consola:
    
    -   Una primera simulación “SIN Eve” (típicamente ≈50 % de coincidencia, unos 7–8 bits de clave en 15 rondas).
        
    -   Una segunda simulación “CON Eve” (muchos menos bits válidos, p. ej. 2–4 de 15, según lo aleatorio).
        

----------

## 2. Interfaz Web Interactiva (`index.html`)

### Objetivo de la Web

Crear una experiencia visual y didáctica que permita a cualquier persona **lanzar monedas virtuales** para simular BB84:

-   Mostrar cómo Alice y Bob eligen bases con azar.
    
-   Ver en tiempo real los bits que se transfieren.
    
-   Incluir la opción de que Eve intercepte y medir el impacto en la generación de la clave.
    
-   Presentar la clave secreta paso a paso junto con la historia de todas las rondas.
    

### Estructura y Funcionamiento

1.  **Controles en la parte superior**:
    
    -   Checkbox “Incluir a Eve”: al activarlo, cada ronda considerará que Eve intercepta antes de Bob.
        
    -   Botón “Lanzar Siguiente Ronda”: ejecuta una ronda más (hasta completar 15 rondas).
        
    -   Botón “Reiniciar Simulación”: borra la tabla y la clave, y reinicia todo.
        
2.  **Tabla de historial** (`<table>`):
    
    -   Columnas fijas:
        
        1.  **N°** de ronda
            
        2.  **Alice Bit** (0/1)
            
        3.  **Alice Base** (↕ o ↗)
            
        4.  **Moneda Alice** (animación del lanzamiento)
            
        5.  **Fotón Enviado** (bit que realmente va hacia Bob, desde Alice o desde Eve)
            
        6.  **Eve Base** (↕ o ↗, si Eve está activa)
            
        7.  **Moneda Eve** (0/1 y animación)
            
        8.  **Bob Base** (↕ o ↗)
            
        9.  **Moneda Bob** (0/1 y animación)
            
        10.  **Bob Bit** (bit final que Bob mide)
            
        11.  **Bases coinciden** (sí/no; comparación de bases de Alice vs. bases de Bob)
            
        12.  **Usar?** (sí/no; si “Bases coinciden = sí”, ese bit entra en la clave)
            
3.  **Animación de moneda**:
    
    -   Cada vez que Alice (o Eve/Bob) lanza una moneda, se crea un `<div class="coin spinning">` con un sprite que gira durante 0.6 s.
        
    -   El número `0` o `1` queda en la celda y luego aparece la animación para reforzar la idea de “azar”.
        
4.  **Clave secreta**:
    
    -   Bajo la tabla hay un texto que muestra “Clave secreta actual: ____”.
        
    -   Cada vez que se genera una ronda donde “Usar? = sí”, el bit de Alice se añade a esa cadena y se actualiza en pantalla.
        
5.  **Lógica detallada** (en JavaScript):
    
    -   `flipCoin()` → devuelve 0 o 1 aleatorio.
        
    -   `coinToBase(coin)` → convierte `0 → 'rect' (↕)` y `1 → 'diag' (↗)`.
        
    -   `runNextRound()` (por cada clic de “Lanzar Siguiente Ronda”):
        
        1.  Alice lanza moneda → guarda `(aCoin, aBit = aCoin, aBase)`.
            
        2.  Si “Incluir a Eve” está marcado, Eve también lanza moneda `(eCoin → eBase)` y mide el bit de Alice:
            
            -   Si `eBase == aBase`, `eBit = aBit`;
                
            -   Si no, `eBit = flipCoin()` (aleatorio).
                
        3.  Bob lanza moneda `(bCoin → bBase)` y mide el fotón recibido:
            
            -   El fotón enviado (bit) es `aBit` si no hay Eve, o `eBit` si Eve intercepta.
                
            -   Si `bBase == fotónBase`, `bBit = fotónBit`; sino `bBit = flipCoin()`.
                
        4.  Se registra “Bases coinciden = (aBase == bBase)”.
            
        5.  Si coinciden, se añade el `aBit` a `secretKey` y se marca “Usar? = sí”.
            
        6.  Se agrega una fila a la tabla con todos los datos y se anima cada moneda.
            
    -   `resetSimulation()` vacía todas las variables y la tabla.
        
6.  **Resultados Esperados**:
    
    -   **Sin Eve**: Aproximadamente la mitad de las rondas (alrededor de 7–8 de 15) marcan “Usar? = sí”; la clave final tendrá ese número de bits.
        
    -   **Con Eve**: Normalmente se reduce a 2–4 bits de clave, pues Eve introduce desacuerdos en las bases.
        

----------

## 3. Cómo ejecutar y visualizar

1.  **Simulación Python**:
    
    -   Asegúrate de tener Python 3 instalado.
        
    -   Ejecuta `python bb84_simulation.py` desde la terminal o Jupyter Notebook.
        
    -   Observa la tabla impresa en la consola y los dos escenarios: sin Eve y con Eve.
        
2.  **Interfaz Web**:
    
    -   Guarda el archivo **index.html** en tu computadora.
        
    -   Abre ese archivo con cualquier navegador moderno (Chrome, Firefox, Edge).
        
    -   Marca “Incluir a Eve” si quieres simular ataques o desmárcalo para ver el caso ideal.
        
    -   Haz clic en “Lanzar Siguiente Ronda” 15 veces.
        
    -   Observa cómo se van agregando filas a la tabla y cómo se forma la “Clave secreta actual”.
        
    -   Si terminas las 15 rondas, pulsa “Reiniciar Simulación” para volver a empezar.
        

----------

## 4. Conclusiones y Observaciones

-   **Función del Azar**: El protocolo BB84 depende de decisiones aleatorias de bases (caras/cruces).
    
-   **Bases Coincidentes**: Solo cuando la base de Bob coincide con la base de origen se preserva el bit.
    
-   **Detección de Eve**: Con Eve activa, la tasa de “Usar? = sí” disminuye notablemente. Alice y Bob pueden comparar una porción de los bits sobre un canal público para medir la tasa de error y detectar espionaje.
    
-   **Didáctica**:
    
    -   El script en Python genera datos tabulados que confirman la teoría.
        
    -   La web interactiva “monedas girando” convierte los conceptos cuánticos en un juego visual accesible para usuarios no especialistas.
        

Con esto, se consigue cumplir los objetivos de:

1.  Entender BB84 de forma práctica.
    
2.  Simular cómo el azar protege la clave.
    
3.  Traducir ideas cuánticas a formatos didácticos (código y visual).
    
4.  Mostrar el impacto y la diferencia frente a cifrados clásicos.
    

----------
