import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

config = configparser.ConfigParser()
config.read('mail.ini')

def send_email(receiver_email,subject, msg):
  print('sending an email')
  subject = subject
  body = msg
  sender_email = config['DEFAULT']['email']
  receiver_email = receiver_email
  password = config['DEFAULT']['password']

  # Create a multipart message and set headers
  message = MIMEMultipart()
  message["From"] = sender_email
  message["To"] = receiver_email
  message["Subject"] = subject
  message["Bcc"] = receiver_email  # Recommended for mass emails

  # Add body to email
  message.attach(MIMEText(body, "plain"))

  # Log in to server using secure context and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message.as_string())

#send_email()