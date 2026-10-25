from Crypto.Cipher import DES

def encrypt(data: bytes) -> bytes:
    # CWE-327: Use of a Broken or Risky Cryptographic Algorithm (DES)
    cipher = DES.new(b'8bytekey', DES.MODE_ECB)
    return cipher.encrypt(data)
