import sys
import json

from flask import Flask
app = Flask(__name__)

def format_rust_code(rust_code):
    formatted_code = rust_code.strip()
    return json.dumps(formatted_code)

@app.route("/api/python", methods=['POST'])
def hello_world(rust_code):
    app.logger.info('testing info log')
    print('testing print log', file=sys.stderr)

    formatted_code = format_rust_code(rust_code)
    print(formatted_code)
    return formatted_code






