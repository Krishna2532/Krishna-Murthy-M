from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img=Image.open("C:/Users/krish/OneDrive/Desktop/face attendence/face images/main1.webp")
        img=img.resize((1530,720))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=50,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email:m39927559@gmail.com",font=("times new romen",20,"bold"),bg="white")
        dev_label.place(x=585,y=130)


        

        

        

        












if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()