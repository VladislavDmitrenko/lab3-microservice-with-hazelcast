from flask import Flask, request

app = Flask(__name__)

messages = []

@app.route('/messages', methods=['POST'])
def add_message():
    message = request.json.get('message')
    if message:
        messages.append(message)
        return 'Message added successfully', 200
    else:
        return 'Invalid message format', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)