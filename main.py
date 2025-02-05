from tkinter import*
from time import strftime
from datetime import datetime
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recogination import Face_Recongnition
from attendance import Attendance
from developer import Developer
from help import Help


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




    




if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

