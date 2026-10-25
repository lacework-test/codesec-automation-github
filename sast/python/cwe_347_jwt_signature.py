import jwt

def read_claims(token: str, key: str) -> dict:
    # CWE-347: Improper Verification of Cryptographic Signature (signature check disabled)
    return jwt.decode(token, key, algorithms=["HS256"], options={"verify_signature": False})
