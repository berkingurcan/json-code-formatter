import sys
import json
from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
CORS(app)

def format_rust_code(rust_code):
    formatted_code = rust_code.strip()
    return json.dumps(formatted_code)

@app.route("/api/python", methods=['POST'])
def format():
    app.logger.info('testing info log')
    print('testing print log', file=sys.stderr)
    rust_code = request.get_json()['rust_code']

    formatted_code = format_rust_code(rust_code)
    print(formatted_code)
    return jsonify(formatted_code)






