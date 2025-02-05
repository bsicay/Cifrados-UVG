# Investigación: Cifrado de César

El **Cifrado de César** es uno de los métodos de cifrado más antiguos y sencillos. Se atribuye su creación a Julio César, quien lo utilizaba para proteger sus comunicaciones militares.

## Historia Breve

- **Época**: Siglo I a. C.  
- **Personaje**: Julio César, general y estadista de la República romana.  
- **Uso Original**: César desplazaba cada letra del alfabeto en 3 posiciones para ofuscar sus mensajes. De esta manera, si el texto era interceptado, resultaba más difícil de leer por los enemigos.  
- **Relevancia Histórica**: Considerado uno de los primeros cifrados de sustitución monoalfabética.

## Ejemplo de Aplicación

Imaginemos que queremos cifrar la palabra **"CRYPTO"** con un desplazamiento de 3.

1. **Alfabeto** (en mayúsculas para simplificar):  
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

2. **Desplazamiento de 3**:  
- A → D  
- B → E  
- C → F  
- ...  
- X → A  
- Y → B  
- Z → C  

3. **Texto original**:
C R Y P T O


4. **Texto cifrado** (aplicando +3 posiciones):  
- C → F  
- R → U  
- Y → B  
- P → S  
- T → W  
- O → R  

**Mensaje Cifrado**: **FUBSWR**

Para **descifrar**, se procede con la operación inversa (desplazar 3 posiciones hacia atrás en el alfabeto).

## Ventajas

1. **Simplicidad**  
- Muy fácil de entender y aplicar, incluso a mano.  
2. **Rapidez**  
- Apenas requiere recursos de cómputo.  
3. **Uso Didáctico**  
- Ideal para enseñar los fundamentos de la criptografía y para ejercicios académicos.

## Vulnerabilidades

1. **Espacio de Claves Limitado**  
- Solo existen 26 posibles desplazamientos (en el alfabeto en inglés) o 27/28 en otros alfabetos (si incluimos la "Ñ" en español).  
2. **Análisis de Frecuencia**  
- Permite al atacante determinar la clave si se conocen las frecuencias típicas de cada letra en el idioma.  
3. **Susceptible a Fuerza Bruta**  
- Con tan pocas claves, es sencillo probar todas las posibilidades hasta encontrar el texto original.

## Conclusión

El **Cifrado de César** es de gran importancia histórica y educativa. Aunque su simplicidad lo hace poco seguro en la actualidad, constituye una pieza fundamental para entender cómo surgieron los cifrados de sustitución y cómo fueron evolucionando hacia métodos mucho más complejos y resistentes a ataques criptográficos.




