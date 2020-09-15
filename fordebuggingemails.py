# this code is only applicable for debugging

import smtplib # importing smtp
from email.message import EmailMessage
import imghdr

"""
go to the terminal and write: (for making a debugging server)
python3 -m smtpd -c DebuggingServer -n localhost:1025, 1025 is the port number

if it says python3 not recognize then replace python3 with python and run it again
"""

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

# to attach files
with open('senditemail.py','r') as f:
	file_data = f.read() # getting data
	file_type = imghdr.what(f.name) # getting the extension
	file_name = f.name # getting the file name
msg.add_attachment(file_data, filename=file_name) # attaching the file to the email adress

# only applicable for debugging purposes, enter the port number which you chose
with smtplib.SMTP('localhost', port=1025) as smtp:		
	smtp.send_message(msg) # sending the message 
	
