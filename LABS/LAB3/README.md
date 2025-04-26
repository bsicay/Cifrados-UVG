# 🔐 Laboratorio de Criptografía Aplicada

Este laboratorio guiado muestra, paso a paso, cómo **no** implementar un sistema criptográfico y cuál es la forma correcta de hacerlo.  
Trabajarás con AES (ECB / CBC), ChaCha20, captura de tráfico con Wireshark y un mini‑ransomware simulado.

---

## 📍 Objetivos

| # | Objetivo |
|---|----------|
| ✅ | Implementar AES en modos **ECB** y **CBC** y comprobar sus efectos. |
| ✅ | Aplicar **ChaCha20** como cifrado de flujo y medir su rendimiento. |
| ✅ | Analizar por qué **ECB** (y mal uso de **CBC**) filtra patrones en imágenes. |
| ✅ | Capturar y estudiar tráfico cifrado con **Wireshark**. |
| ✅ | Simular un ataque de ransomware y discutir buenas prácticas de gestión de claves. |

---

## 🛠 Recursos necesarios

| Recurso | Descripción |
|---------|-------------|
| **Ubuntu VM** ó contenedor **Docker** | Con Python 3 y *PyCryptodome* instalado (`pip install pycryptodome`). |
| **Imagen BMP / PPM** | Sugerencia: `tux.ppm` incluida en `part1/`. |
| **Wireshark** | Para esnifar el tráfico de red en la Parte 2. |

---

## 📑 Estructura del repositorio

```
.
├── part1/          # scripts y datos para imágenes ECB vs CBC
├── part2/          # cliente/servidor TCP cifrados (socket)
├── part3/          # benchmark AES-CBC vs ChaCha20
├── part4/          # ransomware simulado (encrypt_folder.py, decrypt_folder.py)
└── resultados.ipynb  # Jupyter con gráficos y respuestas
```

---

## 📌 Parte 1 · Rompiendo ECB en Imágenes
**Escenario:** un usuario guarda imágenes sensibles cifradas con AES‑ECB.

1. Convertir la imagen a escala de grises.  
2. Cifrar con **AES‑ECB** → `encrypted_ecb.png`.  
3. Cifrar con **AES‑CBC** (IV aleatorio) → `encrypted_cbc.png`.  
4. Comparar las tres.

**Reflexión**

* ¿Por qué ECB revela patrones?  
* ¿Cómo cambia con CBC?  
* ¿Es seguro usar ECB en datos estructurados?

---

## 📌 Parte 2 · Capturando Cifrado en Red con Wireshark
**Escenario:** mensajes AES‑CBC se envían por TCP.

1. Ejecuta `socket_server.py` (PC A).  
2. Ejecuta `socket_client.py` (PC B).  
3. Captura puerto 8080 en Wireshark.

**Reflexión**

* ¿Puede verse que es AES‑CBC?  
* ¿Cómo proteger mejor la comunicación?

---

## 📌 Parte 3 · Cifrado de Flujo con ChaCha20
**Escenario:** el sistema cambia AES por **ChaCha20**.

1. Implementar cifrado/descifrado con ChaCha20.  
2. Comparar tiempos y memoria contra AES‑CBC (gráficas).

**Reflexión**

* ¿Cuál es más rápido?  
* ¿Cuándo usar ChaCha20 en lugar de AES?

---

## 📌 Parte 4 · Ransomware Simulado
**Escenario:** un atacante cifra archivos con AES.

1. `encrypt_folder.py` cifra `.txt` y crea `keyfile.json`.  
2. `decrypt_folder.py` restaura los archivos.

**Reflexión**

* ¿Cómo evitar ransomware?  
* Importancia de custodiar las claves correctamente.

---

## 📊 Resultados
Todos los experimentos, gráficos y respuestas están documentados en **`resultados.ipynb`**.
