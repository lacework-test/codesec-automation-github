from flask import Flask, make_response

app = Flask(__name__)

@app.route('/api/data')
def data():
    resp = make_response("data")
    # CWE-346: Origin Validation Error (any origin allowed)
    resp.headers['Access-Control-Allow-Origin'] = "*"
    return resp
