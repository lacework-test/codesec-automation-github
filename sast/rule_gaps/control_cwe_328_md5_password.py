import hashlib

def hash_password(password: str) -> str:
    # Control: detected today (CWE-328). Makes sure the PR gets a SAST comment.
    return hashlib.md5(password.encode()).hexdigest()
