import hashlib

def hash_password(password: str) -> str:
    # CWE-328: Use of Weak Hash (MD5 on a credential)
    return hashlib.md5(password.encode()).hexdigest()
