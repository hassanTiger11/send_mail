from crypt import methods
from flask import Flask, jsonify, request
from mail import send_email

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/send_email", methods=["POST"])
def send_email():
    print(request.json)
    data = request.json
    if(data.sender_email != ''
    and data.subject !=''
    and data.msg !=''
    and data.receiver_email != ''
    and data.password != ''):
        sender_email = data.sender_email
        subject = data.subject
        body = data.msg
        receiver_email = data.receiver_email
        password = data.password
        send_email(sender_email, password, receiver_email,subject, body)
        return 'successful'

    else:
        return f'missing args\n'
