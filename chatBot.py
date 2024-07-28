import json
import random
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd3b26b548e218b5eb4e83205fcd839f051ecc76f25f73199'
socketio = SocketIO(app)

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    msg = data.get('message', '')  # Extract the message text
    response = get_response(msg)
    emit('response', {'message': response})

def get_response(msg):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in msg.lower():
                return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that. Can you please rephrase?"


if __name__ == '__main__':
    socketio.run(app, debug=True)
