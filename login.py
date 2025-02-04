from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import mysql.connector
from time import strftime
from datetime import datetime
import tkinter
import os
from student import Student
from train import Train
from face_recogination import Face_Recongnition
from attendance import Attendance
from developer import Developer
from help import Help


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg_image = Image.open("face images/main.webp")
        self.bg = ImageTk.PhotoImage(self.bg_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)


        img1 = Image.open("face images/login.jpg")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)  # Fixed resize format
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(frame, image=self.photoimg1, bg="black", borderwidth=0)  # Added `frame` as parent
        lbl_img1.place(x=120, y=20, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="white",fg="black")
        get_str.place(x=95,y=120)


        #Lables


        username_lbl = Label(frame, text="Username", font=("times new roman", 14, "bold"), bg="white", fg="black")
        username_lbl.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 14, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 14, "bold"), bg="white", fg="black")
        password_lbl.place(x=70, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 14, "bold"), show="*")  # show="*" will mask the password input
        self.txtpass.place(x=40, y=245, width=270)
      #==================Icone Pack===============

        img2 = Image.open("face images/login.jpg")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)  # Fixed resize format
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimg2, bg="black", borderwidth=0)  # Added `frame` as parent
        lbl_img2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("face images/pass2.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)  # Fixed resize format
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimg3, bg="black", borderwidth=0)  # Added `frame` as parent
        lbl_img3.place(x=650, y=390, width=25, height=25)


        #Login button
    
        b1=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bg="dark blue",fg="white",relief=RIDGE,activeforeground="white",activebackground="dark blue")
        b1.place(x=110,y=300,width=120,height=35)

        #register button
    
        reg=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,bg="white",fg="black",relief=RIDGE,activeforeground="white",activebackground="white")
        reg.place(x=15,y=350,width=160)


        #forgetpassword button
    
        f1=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bg="white",fg="black",relief=RIDGE,activeforeground="white",activebackground="white")
        f1.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    #============Login function========

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="krishna" and self.txtpass.get()=="Krishna":
            messagebox.showinfo("Success","Welcome to Attendance Management System using Face Recognition System")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='888@Krishna',database='krishna')
            my_cursor=conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            values = (self.txtuser.get(), self.txtpass.get())  # Fix: Use correct entry fields
            my_cursor.execute(query, values)                                                    
            row=my_cursor.fetchone()
            if row is NONE:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='888@Krishna',database='krishna')
                my_cursor=conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "Email not found. Please enter a valid registered email.")
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")
                    

            finally:
                conn.close()
                   


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #================variable===========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contant=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        self.bg_image = Image.open("face images/main.webp")
        self.bg = ImageTk.PhotoImage(self.bg_image)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


        self.bg_image = Image.open("face images/top 1.jpeg")
        self.bg = ImageTk.PhotoImage(self.bg_image)
        left_lbl = Label(self.root, image=self.bg)
        left_lbl.place(x=50, y=100, width=470, height=550)



        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER USER",font=("times new roman",20,"bold"),bg="white",fg="black")
        register_lbl.place(x=20,y=20)



        #============Labels & Entry fields=======================
        fname=Label(frame,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)


        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new romen",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="LAST NAME",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)


        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new romen",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)


        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)


        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contant,font=("times new romen",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)


        email=Label(frame,text="Email ID",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)


        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new romen",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)


        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new romen",15,"bold"),state="readonly",width=20)
        self.combo_security_Q["values"]=("Select ","Your Birth Place","Your Nick Name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)


        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new romen",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)



        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)


        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new romen",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)


        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new romen",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)



        #=====================checkButton==========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Conditions",font=("times new roman",12,"bold"),bg="white",fg="black",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)



        #===================buttons===========
        img=Image.open("face images/button1.jpg")
        img = img.resize((300, 60))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=30,y=440,width=300)

        img1=Image.open("face images/button2.jpg")
        img1 = img1.resize((300, 60))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b2.place(x=440,y=440,width=300)


    def register(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwor And Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms and Condition")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='888@Krishna',database='krishna')
                my_cursor=conn.cursor()
                query=("Select* from register where email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error","User already exit,Please try another email")
                else:
                    my_cursor.execute("INSERT INTO register (fname, lname, contant, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)" ,(
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contant.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass.get(),
                                                                                                ))
                conn.commit()
                messagebox.showinfo("Sucess","Register Successfull")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                conn.close()




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open("face images/top 2.jpeg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        img1=Image.open("face images/top 1.jpeg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        img2=Image.open("face images/top 3.jpeg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)




       #bg image 
        img3=Image.open("face images/main.webp")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #========time===========
        def time():
            string = strftime('%H:%M:%S  %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",12,"bold"),bg="white",fg="black")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open("face images/student1.png")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=220,height=220)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=150,y=300,width=220,height=40)



        
        # face detector button
        img5=Image.open("face images/face.jpeg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.Face_Recongnition)
        b1.place(x=450,y=100,width=220,height=220)

        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.Face_Recongnition,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=450,y=300,width=220,height=40)



        # Attendence button
        img6=Image.open("face images/attendance.jpeg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=750,y=100,width=220,height=220)

        b1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=750,y=300,width=220,height=40)


        # Help disk button
        img10=Image.open("face images/helpdisk.jpeg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.help)
        b1.place(x=1050,y=100,width=220,height=220)

        b1=Button(bg_img,text="Help disk",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=1050,y=300,width=220,height=40)



        #train face button
        img7=Image.open("face images/trainface.png")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=350,width=220,height=220)

        b1=Button(bg_img,text="Train Face",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=150,y=550,width=220,height=40)



        
        # Photo button
        img8=Image.open("face images/photo.jpeg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=350,width=220,height=220)

        b1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=450,y=550,width=220,height=40)



        # developer button
        img9=Image.open("face images/developer.png")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.developer)
        b1.place(x=750,y=350,width=220,height=220)

        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=750,y=550,width=220,height=40)


        # Exit button
        img11=Image.open("face images/exit.jpeg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1050,y=350,width=220,height=220)

        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1.place(x=1050,y=550,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recongnition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    #=================Function Buttons===================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def Face_Recongnition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recongnition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




        



if __name__ == "__main__":
    main()