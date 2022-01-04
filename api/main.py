
from flask import *
app = Flask(__name__)

@app.route('/')
def health_check():
    response = make_response(
        jsonify(
            {
                "status": True, 
            }
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/hello')
def hello_world():
    response = make_response(
        jsonify(
            {
                "hello": "world", 
            }
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
