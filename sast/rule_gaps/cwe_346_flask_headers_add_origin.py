from flask import Flask, make_response

app = Flask(__name__)

@app.route('/api')
def api():
    resp = make_response("data")
    # CWE-346 gap (COD-7391): wildcard origin set with headers.add
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp
