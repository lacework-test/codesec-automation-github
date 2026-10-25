from Crypto.PublicKey import RSA

def generate_key() -> bytes:
    # CWE-326: Inadequate Encryption Strength (RSA key shorter than 2048 bits)
    key = RSA.generate(1024)
    return key.export_key()
