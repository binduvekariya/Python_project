from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'binduvekariya0750@gmail.com'
#email_password = password

email_receiver = 'bagido5905@fgvod.com'

subject = "dont forget to subscribe"
body = """
when you watch a video, please hit subscribe
"""
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

contex = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contex) as smtp:
    smtp.login(email_sender,) #email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
