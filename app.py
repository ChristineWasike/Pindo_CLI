from flask import Flask, jsonify

app = Flask(__name__)

#route
@app.route('/')
def ping():
    return jsonify({
        'status': 200,
        'message': 'success',
        'payload': 'pong'
    })

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')