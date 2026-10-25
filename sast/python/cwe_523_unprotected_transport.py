import requests

def send_credentials(user: str, password: str):
    # CWE-523: Unprotected Transport of Credentials (HTTP basic auth over plain HTTP)
    return requests.get("http://example.com/login", auth=(user, password))
