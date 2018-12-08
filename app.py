from flask import Flask, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

#new
class Config:
    BASE_URL = 'http://178.128.165.87'

class Send(Config):
    def __init__(self, token, to, text, sender='MPESA'):
        self.token = token
        self.to = to
        self.text = text
        self.sender = sender
        self.url = '{}/sms/'.format(Config.BASE_URL)
    
    def sms(self):
        payload = {
            'to': self.to,
            'text': self.text,
            'sender': self.sender
        }

        r = request.post{
            self.url,
            auth = HTTPBasicAuth(self.token, ''),
            json = payload
        }
        return r.json()

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