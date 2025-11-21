import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize SMTP connection
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
email=input("Enter your email: ")
password=input("Enter your password: ")
smtp.login(email, password)

# Create the email message
msg = MIMEMultipart()
msg['Subject'] = 'Subject goes here'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'receiver_email@example.com'

# Add the actual message text
body = "Hello, this is an automatic email sent using Python!"
msg.attach(MIMEText(body, 'plain'))

# Send the email
smtp.sendmail('your_email@gmail.com', 'receiver_email@example.com', msg.as_string())

# Close the SMTP connection
smtp.quit()
