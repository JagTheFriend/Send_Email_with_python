# import necessary libraries

import smtplib 
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Python.org email' # that is the topic
msg['From'] = 'jagadish.mohanty@iesmail.com' # your email
msg['To'] = 'jagadish.mohanty@iesmail.com' # receivers' email

msg.set_content('This was sent using python') # this is the body

# to attach files
with open('senditemail.py','r') as f:
	file_data = f.read() # getting data
	file_type = imghdr.what(f.name) # getting the extension
	file_name = f.name # getting the file name

msg.add_attachment(file_data, filename=file_name) # attaching the file to the email adress

# suitable to gmail
with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
    smtp.login(user='jagadish.mohanty@iesmail.com',password='mypassword@12',initial_response_ok=True) # logging in
    
    smtp.send_message(msg) # sending the message

