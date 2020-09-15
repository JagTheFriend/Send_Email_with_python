import smtplib # importing smtp


# only applicable for gmail
with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
	smtp.ehlo() # identifies ourselves with the mail server, gets called automatically

	# encrypt traffic,making it "https"
	smtp.starttls()

	# re run ehlo to identify ourselves with encryption
	smtp.ehlo()

	# login to the server
	smtp.login(user="your_email@gmail.com", password="your_password",initial_response_ok=True)

	# the subject/title
	subject = 'Sending email using python'

	# main body
	body = 'Did you know that you could send email using python ?'

	# the message
	msg = f'Subject: {subject}\n\n{body}'

	# now send the mail, Sender -> Receiver -> msg
	smtp.sendmail('your_email@gmail.com', 'Reciever_email@gmail.com', msg) 
