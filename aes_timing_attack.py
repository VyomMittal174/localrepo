import time
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import matplotlib.pyplot as plt

# AES encryption with simulated timing leak
def aes_encrypt_with_timing_leak(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    start_time = time.perf_counter()
    ciphertext = cipher.encrypt(plaintext)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    # Introduce artificial leak based on the first byte
    simulated_leak = plaintext[0] * 1e-7  # exaggerate for visibility
    return ciphertext, elapsed_time + simulated_leak

# Generate random AES key
key = get_random_bytes(16)
plaintexts = [bytes([i]) + b'\x00' * 15 for i in range(256)]

timings = []

# Encrypt many different plaintexts and measure timing
for pt in plaintexts:
    _, timing = aes_encrypt_with_timing_leak(key, pt)
    timings.append(timing)

# Plot timings
plt.figure(figsize=(10, 6))
plt.plot(range(256), timings, marker='o', linestyle='-', markersize=3)
plt.title('Simulated AES Timing Attack')
plt.xlabel('First Byte of Plaintext')
plt.ylabel('Encryption Time (seconds)')
plt.grid(True)
plt.show()
