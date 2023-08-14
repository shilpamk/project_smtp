import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

sender_email = os.environ.get('USER_EMAIL')
receivers_email = ['smtp2023.test2@gmail.com', 'abc@gmail.com']

appPassword = os.environ.get('APP_PASSWORD')

message = EmailMessage()
message['From'] = sender_email
message['To'] = receivers_email
message['Subject'] = 'Testing smtp'
message.set_content('Attachments included!')

os.chdir('dummy_files')
all_files = os.listdir()

for file in all_files:
   with open(file, 'rb') as f:
      f_data = f.read()
      f_name = f.name

      message.add_attachment(f_data, maintype='application', subtype='octet-strem', filename=f_name)


try:
   with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        
        server.login(sender_email, appPassword)  
        print('Login Success') 

        server.send_message(message)
        print(f'Email has been sent to {receivers_email}')
   
except Exception as e:
   print (e)