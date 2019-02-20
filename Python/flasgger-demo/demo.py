from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


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
