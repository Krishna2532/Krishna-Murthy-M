from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==============varaibles==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        img=Image.open("face images/top 2.jpeg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        img1=Image.open("face images/top 1.jpeg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)


        #bg image 
        img3=Image.open("C:/Users/krish/OneDrive/Desktop/face attendence/face images/main.webp")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendance",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=12,y=55,width=1500,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attencance Details",font=("times new romen",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open("C:/Users/krish/OneDrive/Desktop/face attendence/face images/studentdetailes.jpeg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(bg_img,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=33,y=230,width=715,height=330)


        #lables and entries
        attendanceId_label=Label(left_inside_frame,text="Attendance Id",font=("times new romen",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5)

        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new romen",11,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5)
        #roll

        rollLabel=Label(left_inside_frame,text="Roll",font=("times new romen",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new romen",11,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #name

        nameLabel=Label(left_inside_frame,text="Name",font=("times new romen",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new romen",11,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #Departement

        depLabel=Label(left_inside_frame,text="Departement",font=("times new romen",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new romen",11,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #time

        timeLabel=Label(left_inside_frame,text="Time",font=("times new romen",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new romen",11,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #Date

        dateLabel=Label(left_inside_frame,text="Date",font=("times new romen",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new romen",11,"bold"))
        atten_date.grid(row=2,column=3,pady=8)


        #Attendance

        attendanceLabel=Label(left_inside_frame,text="Attendance",font=("times new romen",12,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)

        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        #Button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=200,width=700,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new romen",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new romen",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new romen",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new romen",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        #right label frame

        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attencance Details",font=("times new romen",12,"bold"))
        RIGHT_frame.place(x=750,y=10,width=740,height=580)

        table_frame=Frame(RIGHT_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=7,y=5,width=720,height=470)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")   

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #=================================fetch data====================


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

#====import csv====
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],parent=self.root)
        if not fln:
            return
        try:
            with open(fln,newline='') as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for row in csvread:
                    mydata.append(row)
            self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file:\n{str(e)}", parent=self.root)

#==========export csv===========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO DATA", "NO DATA found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for row in mydata:
                    exp_write.writerow(row)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as e:
                messagebox.showerror("Error", f"Due To:\n{str(e)}", parent=self.root)

    #=================
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])     

    #============reset=======
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def update_data(self):
        """Updates the selected row with modified data."""
        selected = self.AttendanceReportTable.focus()
        if not selected:
            messagebox.showerror("Error", "No record selected!", parent=self.root)
            return

        updated_row = [
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ]

        self.AttendanceReportTable.item(selected, values=updated_row)
        messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)

        

        




       













if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()