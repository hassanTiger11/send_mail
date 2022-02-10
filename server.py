from crypt import methods
from flask import Flask, jsonify, request
from mail import send_email

app = Flask(__name__)

@app.route("/")
def hello_world():
    print('hello')
    return "<p>Hello, World!</p>"

@app.route("/send_email", methods=["POST"])
def send_mail():
    print(f' ######## {request.get_json()} #######')
    data = request.get_json()
    if(
    data['subject'] !=''
    and data['body'] !=''
    and data['receiver_email'] != ''
    ):
        
        subject = data['subject']
        body = data['body']
        receiver_email = data['receiver_email']
        
        send_email(receiver_email,subject, body)
        return 'successful'

    else:
        return f'missing args\n'

