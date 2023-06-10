import requests

messages = ['msg1', 'msg2', 'msg3', 'msg4', 'msg5', 'msg6', 'msg7', 'msg8', 'msg9', 'msg10']

for message in messages:
    response = requests.post('http://127.0.0.1:8000/messages', json={'message': message})
    if response.status_code == 200:
        print(f"Message '{message}' added successfully")
    else:
        print(f"Failed to add message '{message}'")