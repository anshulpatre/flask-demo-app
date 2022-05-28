from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1 style="text-align: center;">Flask Demo App Working Fine</h1>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
