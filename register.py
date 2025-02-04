from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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


                
        
        














        










if __name__ == "__main__":
    root = Tk()
    obj = Register(root)  
    root.mainloop()