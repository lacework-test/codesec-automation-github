import random
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/login')
def login():
    resp = make_response("Logged in")
    # CWE-338: Weak PRNG used for a session token
    session_token = str(random.random())
    resp.set_cookie('session_token', session_token, secure=True, httponly=True, samesite='Strict')
    return resp
