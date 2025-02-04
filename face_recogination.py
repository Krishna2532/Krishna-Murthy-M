from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy as np





class Face_Recongnition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Face Recongnition",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"face images/face8.jpg")
        img_top=img_top.resize((1530,760))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=760)


        b1_1=Button(self.root,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_1.place(x=650,y=600,width=200,height=40)


    #==============attendance==========================
    def mark_attendance(self,i,r,n,d):
        with open("krishna.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    #===============================Face Recognition============
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,colour,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            
            

            for(x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))

                conn=mysql.connector.connect(host='localhost',username='root',password='888@Krishna',database='krishna')
                my_cursor=conn.cursor()

                my_cursor.execute("select name FROM student where ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                
                my_cursor.execute("select roll FROM student where ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select ID FROM student where ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select ID FROM student where ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                



                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"UnKnown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(1)
        if not video_cap.isOpened():
            print("Error: Could not open camera.")
        else:
            print("camera successfully opened.")

        while True:
            ret,img=video_cap.read()
           
            if not ret:
                print("Error:Failed to capture image.")
                break
            img=recognize(img,clf,faceCascade)
            
            cv2.imshow("Welcome To FaceRecongnition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()






        
if __name__ =="__main__":
    root=Tk()
    obj=Face_Recongnition(root)
    root.mainloop()