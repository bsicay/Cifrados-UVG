import time, tracemalloc, os, json, matplotlib.pyplot as plt, numpy as np
from Crypto.Cipher import ChaCha20, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

BLOCK = 16

def bench(size_bytes, iterations=50):
    data = os.urandom(size_bytes)
    key_aes = get_random_bytes(32)
    key_chacha = get_random_bytes(32)
    iv = get_random_bytes(16)
    nonce = get_random_bytes(8)

    # ---- AES-CBC ----
    tracemalloc.start()
    t0 = time.perf_counter()
    for _ in range(iterations):
        cipher = AES.new(key_aes, AES.MODE_CBC, iv)
        ct = cipher.encrypt(pad(data, BLOCK))
        cipher_dec = AES.new(key_aes, AES.MODE_CBC, iv)
        pt = unpad(cipher_dec.decrypt(ct), BLOCK)
    t_aes = (time.perf_counter() - t0) / iterations
    _, peak_aes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # ---- ChaCha20 ----
    tracemalloc.start()
    t0 = time.perf_counter()
    for _ in range(iterations):
        cipher = ChaCha20.new(key=key_chacha, nonce=nonce)
        ct = cipher.encrypt(data)
        cipher_dec = ChaCha20.new(key=key_chacha, nonce=nonce)
        pt = cipher_dec.decrypt(ct)
    t_ch = (time.perf_counter() - t0) / iterations
    _, peak_ch = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {"size": size_bytes/1024, "aes_time": t_aes*1000, "ch_time": t_ch*1000,
            "aes_mem": peak_aes/1024, "ch_mem": peak_ch/1024}

sizes = [1024, 10*1024, 100*1024]
res = [bench(s) for s in sizes]

# plotting
x = np.arange(len(sizes)); w=0.35
aes_t = [r["aes_time"] for r in res]
ch_t = [r["ch_time"] for r in res]
aes_m = [r["aes_mem"] for r in res]
ch_m = [r["ch_mem"] for r in res]
labels = [f"{r['size']:.0f} KB" for r in res]

plt.figure(figsize=(8,4))
plt.bar(x-w/2, aes_t, w, label="AES-CBC")
plt.bar(x+w/2, ch_t, w, label="ChaCha20")
plt.ylabel("ms (promedio cifrar+descifrar)")
plt.xticks(x, labels)
plt.title("Tiempo medio por operación")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,4))
plt.bar(x-w/2, aes_m, w, label="AES-CBC")
plt.bar(x+w/2, ch_m, w, label="ChaCha20")
plt.ylabel("Memoria pico (KB)")
plt.xticks(x, labels)
plt.title("Memoria utilizada")
plt.legend()
plt.tight_layout()
plt.show()
