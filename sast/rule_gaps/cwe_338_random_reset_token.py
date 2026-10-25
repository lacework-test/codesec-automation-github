import random
import string

def make_reset_token() -> str:
    # CWE-338 gap (COD-7393): password-reset token from a weak PRNG
    reset_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return reset_token
