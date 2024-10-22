import socket
import threading
import util_aes_256

key = 'gAe8kBQZZPrN95H9TpceCVM5wQ6F1k1F'
iv = 'abvuTZ2EPElfmQ8U'
plain_text = "홍길동"

cipher = util_aes_256.Cipher(key, iv)

encrypted = cipher.encrypt(plain_text)

decrypted = cipher.decrypt(encrypted)

print(f"===result===")
print(f"{plain_text}")
print(f"{encrypted}")
print(f"{decrypted}")