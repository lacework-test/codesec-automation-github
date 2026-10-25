import requests

def profile(token: str):
    # CWE-523 gap (COD-7392): bearer token in a header over plain HTTP
    return requests.get("http://example.com/me", headers={"Authorization": f"Bearer {token}"})
