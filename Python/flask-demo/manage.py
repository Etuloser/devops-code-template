from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def endpoint():
    return jsonify({'endpoint': '/'})


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)