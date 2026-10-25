from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CWE-346 gap (COD-7391): flask-cors default allows every origin
CORS(app)
