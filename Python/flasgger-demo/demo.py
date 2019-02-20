from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
template = {
    "swagger": "2.0",
    "info": {
        "title": "My API",
        "description": "API for Test",
        "version": "0.0.1"
    },
    "host": "localhost:5000",  # overrides localhost:500
    "basePath": "/",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
}

swagger = Swagger(app, template=template)


@app.route('/demo')
def demo():
    """
    Simple test
    ---
    responses:
      200:
        description: successful operation
      500:
        description: error operation
    """
    result = 'just for test'
    return jsonify(result)


app.run(debug=True)
