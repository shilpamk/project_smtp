import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender_email = os.environ.get('USER_EMAIL')
receivers_email = 'smtp2023.test2@gmail.com'

appPassword = os.environ.get('APP_PASSWORD')

message = EmailMessage()
message['From'] = sender_email
message['To'] = receivers_email
message['Subject'] = 'Testing smtp'
message.set_content('This email has been sent from Python code!')


try:
   with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(sender_email, appPassword)  
        print('Login Success')
        server.send_message(message)
        print(f'Email has been sent to {receivers_email}')
   
except Exception as e:
   print (e)