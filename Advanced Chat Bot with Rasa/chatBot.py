import json
import requests
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    msg = data.get('message', '')
    response = get_rasa_response(msg)
    emit('response', {'message': response})

def get_rasa_response(msg):
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {
        "sender": "user",
        "message": msg
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(rasa_url, data=json.dumps(payload), headers=headers)
    response_data = response.json()
    if response_data:
        return response_data[0].get('text', "I'm sorry, I don't understand that.")
    return "I'm sorry, I don't understand that."

if __name__ == '__main__':
    socketio.run(app, debug=True)
