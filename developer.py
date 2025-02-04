from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DELEVOPER",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img=Image.open("C:/Users/krish/OneDrive/Desktop/face attendence/face images/main.webp")
        img=img.resize((1530,720))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)


        

        #frame

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=70,y=50,width=300,height=300)


        img1=Image.open("C:/Users/krish/OneDrive/Desktop/face attendence/face images/pass.jpg")
        img1=img1.resize((200,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=55,y=20,width=200,height=200)

        #============developer info==========
        dev_label=Label(main_frame,text="Hello my name is Krishna Murthy M",font=("times new romen",12,"bold"),bg="white")
        dev_label.place(x=10,y=230)

        












if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()