from flask import Flask, make_response

app = Flask(__name__)

@app.route('/api')
def api():
    resp = make_response("data")
    # Not an origin issue: only the allowed methods are a wildcard. Reported as CWE-346 today (COD-7391).
    resp.headers.add('Access-Control-Allow-Methods', "*")
    return resp
