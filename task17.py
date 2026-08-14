import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "nihanthsakalabhaktula@gmail.com"
password = "kfandbdfhbbndqhg"

recipients = [
    "abhiramdumpala4@gmail.com",
    "nihanthsakalabhaktula6@gmail.com",
    "jagadeeshboyalla3384@gmail.com"
]

subject = "Testing Mail"
message = "This is a Test mail, Please Ignore it"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(sender, password)

print("Login Successful")

for recipient in recipients:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server.sendmail(sender, recipient, msg.as_string())

    print(f"Email sent successfully to {recipient}")

server.quit()

print("All emails sent successfully.")
