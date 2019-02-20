# flasgger-demo
> Library reference
>
> [flasgger homepage](https://github.com/rochacbruno/flasgger)
>
> [OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#operation-object)

## init

```shell
# in win
$ virtualenv venv
$ .\venv\Scripts\active
(venv)$ pip install flasgger
```

*demo.py*

```python
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
```

```shell
(venv)$ python demo.py
# then see the page at http://localhost:5000/apidocs/
```

