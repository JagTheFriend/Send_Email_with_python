# import necessary libraries

import smtplib 
import imghdr
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Python.org email' # that is the topic
msg['From'] = 'your@gmail.com' # your email
msg['To'] = 'receivers@gamil.com' # receivers' email

msg.set_content('This was sent using python') # this is the body

msg.add_alternative(
	"""\
	<html>
		<head>
			<h3> Python is very good </h3>
		</head>
	</html>
""",subtype='html')

with open('htmladdedemail.py','r') as f:
	data = f.read()
	name = f.name

	msg.add_attachment(data,filename="Made an email using python and html")

# suitable to gmail
with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:
    smtp.login(user='yourmail@iesmail.com',password='yourpassword',initial_response_ok=True) # logging in
    
    smtp.send_message(msg) # sending the message

