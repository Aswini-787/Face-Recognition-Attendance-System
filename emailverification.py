import smtplib
from random import *
from email.message import EmailMessage
def send():
    global random
    random = randint(10000,999999)
    msg = EmailMessage()
    msg["Subject"] = "Monthly Attendance Report"
    msg["From"] = "Attendence Mananger"
    message = """Subject: OTP For verification

OTP : """+str(random)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, app_password)
    server.sendmail(sender, receiver, message)
    server.quit()

sender = "studenthelper094@gmail.com"
app_password = "bnnh eiss lrvn yxzi"
receiver = ""



print("Email sent!")
