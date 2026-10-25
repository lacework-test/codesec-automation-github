import requests

def login(user: str, password: str):
    # CWE-523 gap (COD-7392): credentials in the form body over plain HTTP
    return requests.post("http://example.com/login", data={"username": user, "password": password})
