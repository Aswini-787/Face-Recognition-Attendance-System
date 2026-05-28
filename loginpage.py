from tkinter import*
import emailverification as ev
import dashboard as db
from tkinter import messagebox
import csv
import os 

# ------------------  Note  ----------------------------
# features to add :
# 1.report
#    i) instead of monthly report can be as a range (class)
#    ii) average over a range (class)
#    iii) specific student over range (student)
# 2.view students (treeview)
# 3.remove students 

def check1():
    f=open("admin.csv","r")
    reader=csv.reader(f)
    for row in reader:
        if row[0]==entry1.get() and row[1]==entry2.get():
            return 1
        
        messagebox.showwarning("Warning", "Enter correct user credentials!")
        return 0

def send_otp():
    global entry3,entry1,entry2,button1
    global text2
    global button2
    while (check1()==0):
        entry1=Entry(frame,width=50,fg="gray34")
        entry1.insert(0,"Enter Name ")
        entry1.place(x=50,y=120)

        entry2=Entry(frame,width=50,fg="gray34")
        entry2.insert(0,"Enter Email Id")
        entry2.place(x=50,y=170)

        button1=Button(frame,text="Send OTP",command=send_otp)
        button1.place(x=300,y=220)
        window.mainloop()


    entry3=Entry(frame,width=50,fg="gray34")
    entry3.insert(0,"Enter OTP")
    entry3.place(x=50,y=220)
    text2=Label(frame,text="OTP sent ! ",bg="#1e1e1e",fg="white",height=3,width=20)
    text2.place(x=130,y=270)
    ev.receiver=entry2.get()
    ev.send()
    button1.destroy()
    button2=Button(frame,text="verify",command=check)
    button2.place(x=300,y=270)
def check():
    otp=entry3.get()
    check_otp(ev.random,otp)

def check_otp(r,otp):
    global text2, button2 , entry1, entry2
    if str(r) == otp:
         f=open("admin.csv","w",newline="")
         header=[entry1.get(),entry2.get()]
         writer=csv.writer(f)
         writer.writerow(header) 
         window.destroy()
         db.main()
        
    else:
        text2.destroy()
        text2=Label(frame,text="OTP incorrect ! ",bg="#1e1e1e",fg="white",height=3,width=20)
        text2.place(x=130,y=270)
        button2.destroy()
        button2=Button(frame,text="resend otp",command=send_otp)
        button2.place(x=300,y=270)


if os.path.isfile("admin.csv"):
    print("file exists")
    window=Tk()
    window.title("Login" )
    window.configure(bg="black")


    window.state("zoomed")


    label1 = Label(window,bg="black")
    label1.place(x=0, y=0, relwidth=1, relheight=1)

#login frame
    frame = Frame(window, bg='#1e1e1e')
    frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=550)

#texts

    text1=Label(frame,text="Login",  font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
    text1.pack(pady=20)

#text2=Label(frame ,text="Name", font=("Arial", 10, "bold"), bg="#1e1e1e", fg="white")
#text2.place(x=100,y=100)

    entry1=Entry(frame,width=50,fg="gray34")
    entry1.insert(0,"Enter Name ")
    entry1.place(x=50,y=120)

    entry2=Entry(frame,width=50,fg="gray34")
    entry2.insert(0,"Enter Email Id")
    entry2.place(x=50,y=170)
    

    button1=Button(frame,text="Send OTP",command=send_otp)
    button1.place(x=300,y=220)
    window.mainloop()


else:
    # so you are to check if the entered email is in admin file if not message box with wrong email id (send_otp func)
    # use try and except in try u put file exists and check for the email except you send the mail and if the mail exist raise a error 
     window.title("Login" )
     window.configure(bg="black")
     window.state("zoomed")

     label1 = Label(window,bg="black")
     label1.place(x=0, y=0, relwidth=1, relheight=1)

#login frame
     frame = Frame(window, bg='#1e1e1e')
     frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=550)

#texts

     text1=Label(frame,text="Login",  font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
     text1.pack(pady=20)

#text2=Label(frame ,text="Name", font=("Arial", 10, "bold"), bg="#1e1e1e", fg="white")
#text2.place(x=100,y=100)

     entry1=Entry(frame,width=50,fg="gray34")
     entry1.insert(0,"Enter Name ")
     entry1.place(x=50,y=120)

     entry2=Entry(frame,width=50,fg="gray34")
     entry2.insert(0,"Enter Email Id")
     entry2.place(x=50,y=170)

     button1=Button(frame,text="Send OTP",command=send_otp)
     button1.place(x=300,y=220)

     button2=Button(frame, text="scan")
     button2.place(x=50,y=220)
window.mainloop()

