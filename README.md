# send_mail
I made this microservice to help me with executing time consuming tasks on a computer. It pushes notifications to my
email upon execution of a command

## Configuration
This microservice needs a sender email and password. So, I used a dockerfile to that do the packaging for me. You can use the docker file included in the repo but you need to build it with your own creditials

## Usage:
You will have to send a post request to you server that contain the email in a json format, example:
`curl -X POST <server url>/<request> -H 'Content-Type: application/json' -d '{"receiver_email":"reciever@email","subject": "test", "body": "test"}'`
