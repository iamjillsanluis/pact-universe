from flask import Flask, Response
import json


app = Flask(__name__)


@app.route("/food")
def index():
    data = {
        'answer': 'yes',
    }

    return Response(
        json.dumps(data),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
