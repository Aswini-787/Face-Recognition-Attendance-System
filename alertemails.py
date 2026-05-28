import smtplib
from tkinter import*
import csv
from random import *
from tkinter import messagebox
def check():
    global receiver
    f=open("dataset.csv","r")
    read=csv.reader(f)
    read=list(read)
    del read[0]
    print(read)
    for i in read:
        percent=int(i[4])*100/int(i[3])
        print(percent)
        if percent<75:
            receiver=i[2]
            send(i[1],percent)
    f.close()
def send(student_name,percent):
    percent=round(percent,2)
    message = """Subject: Attendance Alert

Dear """ + student_name + """,

This is to inform you that your attendance percentage has fallen below the required minimum.

Current Attendance: """ + str(percent) + """%
Required Attendance: 75%

Please attend the upcoming classes regularly to avoid academic issues.

If you have any concerns, please contact your department.

Regards,
Attendance Alert System"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, app_password)
    server.sendmail(sender, receiver, message)
    server.quit()
    messagebox.showinfo("Important Message","Report emailed successfully ! ")
sender = "studenthelper094@gmail.com"
app_password = "bnnh eiss lrvn yxzi"
receiver = ""



