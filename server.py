from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return """<h1 style="text-align: center;color:red;font-size:80px;">Sentiment Analysis</h1>"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
