
########################### import ##############
from tkinter import *
import tkinter as T
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np
from  tkinter import messagebox as m
from PIL import Image
from PIL import ImageTk
import face_recognition
from sklearn import svm
import os
from tkinter import filedialog
import cv2
import pandas as pd
import openpyxl 
import csv
from datetime  import datetime
from PIL import ImageTk,Image
from tabulate import tabulate





########################### Window ##############
w=T.Tk()
fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\pa1.jpg')
re=fi.resize((1000,1000),Image.ANTIALIAS)
b=ImageTk.PhotoImage(re)
l=T.Label(w,image=b)


message = T.Label(
    w, text="Face-Recognition-System Attendenc", fg="black",bg="gray", width=50,
    height=3, font=('times', 25, 'bold'))
 
message.place(x=0, y=20)

################################################  comuter Security A  ##########################
def csa():
  sa= T.Toplevel(w)
# define columns
  columns = ('Name', 'Id', 'Email','Phone Number')
  tree = ttk.Treeview(sa,columns=columns, show='headings')
# define headings
  tree.heading('Name', text='Name')
  tree.heading('Id', text='Id')
  tree.heading('Email', text='Email')
  tree.heading('Phone Number', text='Phone Number')
# generate sample data
  contacts = []
  contacts.append((f'Ahmed Mahfood ', f'1365223 ', f'1365223.sal@utas.edu.om',f'99999999'))
  contacts.append((f'Harry Potter ', f'1111111 ', f'1111111@ugmail.com',f'99990000'))
  contacts.append((f'Ahmed Salim ', f'13652279 ', f'2019393074.sal@utas.edu.om',f'90000000'))
  contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
  contacts.append((f'Nepras AlHinai ', f'133052287 ', f'133052287.sal@utas.edu.om',f'90000003'))
  contacts.append((f'Maram Hamid Said Qatan ', f'2017393037 ', f'017393037.sal@cas.edu.om',f'90000002'))
  contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))

# add data to the treeview
  for contact in contacts:
    tree.insert('', T.END, values=contact)
  def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
  tree.bind('<<TreeviewSelect>>', item_selected)
  tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
  scrollbar = ttk.Scrollbar(sa, orient=T.VERTICAL, command=tree.yview)
  tree.configure(yscroll=scrollbar.set)
  scrollbar.grid(row=0, column=1, sticky='ns')

  sa.title(" list Of Student")
  sa.mainloop()



def file():
    root=T.Tk()
    frame1 = T.LabelFrame(root, text="Excel Data")
    frame1.place(height=250, width=500)

# Frame for open file dialog
    file_frame = T.LabelFrame(root, text="Open File")
    file_frame.place(height=100, width=400, rely=0.65, relx=0)

# Buttons
    button1 = T.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
    button1.place(rely=0.65, relx=0.50)

    button2 = T.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
    button2.place(rely=0.65, relx=0.30)

    button3 = T.Button(file_frame, text="print File", command=lambda: Load_excel_data())
    button3.place(rely=0.65, relx=0.10)

# The file/file path text
    label_file = ttk.Label(file_frame, text="No File Selected")
    label_file.place(rely=0, relx=0)


## Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = T.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
    treescrollx = T.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


    def File_dialog():
       """This Function will open the file explorer and assign the chosen file path to label_file"""
       filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("python files", "*.csv"),("All Files", "*.*")))
       label_file["text"] = filename
       return None


    def Load_excel_data():
       """If the file selected is valid this will load the file into the Treeview"""
       file_path = label_file["text"]
       try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

       except ValueError:
        T.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
       except FileNotFoundError:
        T.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

       clear_data()
       tv1["column"] = list(df.columns)
       tv1["show"] = "headings"
       for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

       df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
       for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
       return None


    def clear_data():
      tv1.delete(*tv1.get_children())
      return None

    T.mainloop()



def CSA():
    path='CSA'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('CSA.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    



def T1():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=csa, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendance",
                     command=CSA, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()


  ################################################   comuter Security B    ##########################
def csb():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

# generate sample data
   contacts = []
   contacts.append((f'Ahmed Mahfood ', f'1365223 ', f'1365223.sal@utas.edu.om',f'99999999'))
   contacts.append((f'Ahmed Salim ', f'13652279 ', f'2019393074.sal@utas.edu.om',f'90000000'))
   contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
   contacts.append((f'Nepras AlHinai ', f'133052287 ', f'133052287.sal@utas.edu.om',f'90000003'))
   contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))

# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()


def CSB():
    path='CSB'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('CSB.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
      



def T2():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=csb, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendence",
                     command=CSB, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Sub Window")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()


 ############################################ G1  ##########
def G1():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

   contacts = []
   contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
   contacts.append((f'Maram Hamid Said Qatan ', f'2017393037 ', f'017393037.sal@cas.edu.om',f'90000002'))
   contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))
   contacts.append((f'Rawan Rashid AlBattashi ', f'2018393036 ', f'2018393036.sal@cas.edu.om',f'96389946'))


# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()




def G11():
    path='GP1'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('GP1.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    

def T8():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=G1, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendance",
                     command=G11, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()



 ################################################### Ethical #########################
def E():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

# generate sample data
   contacts = []
   contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
   contacts.append((f'Maram Hamid Said Qatan ', f'2017393037 ', f'017393037.sal@cas.edu.om',f'90000002'))
   contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))
   contacts.append((f'Rawan Rashid AlBattashi ', f'2018393036 ', f'2018393036.sal@cas.edu.om',f'96389946'))


# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()



def EHN():
    path='EHN'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('EHN.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    


def T3():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=E, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendance",
                     command=EHN, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()


####################################################  G2################################

def G2():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

   contacts = []
   contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
   contacts.append((f'Maram Hamid Said Qatan ', f'2017393037 ', f'017393037.sal@cas.edu.om',f'90000002'))
   contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))
   contacts.append((f'Rawan Rashid AlBattashi ', f'2018393036 ', f'2018393036.sal@cas.edu.om',f'96389946'))


# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()


def GP2():
    path='GP2'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('GP2.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    

  



def T4():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=G2, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendance",
                     command=GP2, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()


######################################################## Innovation #################

def I():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

   contacts = []
   contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
   contacts.append((f'Maram Hamid Said Qatan ', f'2017393037 ', f'017393037.sal@cas.edu.om',f'90000002'))
   contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))
   contacts.append((f'Rawan Rashid AlBattashi ', f'2018393036 ', f'2018393036.sal@cas.edu.om',f'96389946'))
   contacts.append((f'Ahmed Mahfood ', f'1365223 ', f'1365223.sal@utas.edu.om',f'99999999'))
   contacts.append((f'Ayoub Suliman ', f'1315227 ', f'1315227.sal@utas.edu.om',f'90000007'))
   contacts.append((f'Hamad AlHavthy ', f'1315298 ', f'1315298.sal@utas.edu.om',f'90000010'))


# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()




def INS():
    path='INS'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('INS.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    


def T5():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=I, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendance",
                     command=INS,fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()


################################################### NetWork Security  A ###########################
 
def A1():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

   contacts = []
   contacts.append((f'Balqis Jamil Saif AlSadi ', f'2017393046 ', f'2017393046.sal@cas.edu.om',f'90000001'))
   contacts.append((f'Maram Hamid Said Qatan ', f'2017393037 ', f'017393037.sal@cas.edu.om',f'90000002'))
   contacts.append((f'Hiba Musabah AlSalmani ', f'2017393034 ', f'2017393034.sal@cas.edu.om',f'90000004'))
   contacts.append((f'Rawan Rashid AlBattashi ', f'2018393036 ', f'2018393036.sal@cas.edu.om',f'96389946'))
   contacts.append((f'Ahmed Mahfood ', f'1365223 ', f'1365223.sal@utas.edu.om',f'99999999'))
   contacts.append((f'Ayoub Suliman ', f'1315227 ', f'1315227.sal@utas.edu.om',f'90000007'))
  

# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()


def NSA():
    path='NSA'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('NSA.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    



def T6():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=A1, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="Attendance",
                     command=NSA ,fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()

######################################## Network Technology ############################

def N1():
   sb= T.Toplevel(w)
# define columns
   columns = ('Name', 'Id', 'Email','Phone Number')
   tree = ttk.Treeview(sb,columns=columns, show='headings')
# define headings
   tree.heading('Name', text='Name')
   tree.heading('Id', text='Id')
   tree.heading('Email', text='Email')
   tree.heading('Phone Number', text='Phone Number')

   contacts = []
   contacts.append((f'Ahmed Mahfood ', f'1365223 ', f'1365223.sal@utas.edu.om',f'99999999'))
   contacts.append((f'Ahmed Salim ', f'13652279 ', f'2019393074.sal@utas.edu.om',f'90000000'))
   contacts.append((f'Nepras AlHinai ', f'133052287 ', f'133052287.sal@utas.edu.om',f'90000003'))
   contacts.append((f'Ayoub Suliman ', f'1315227 ', f'1315227.sal@utas.edu.om',f'90000007'))
   contacts.append((f'Hamad AlHavthy ', f'1315298 ', f'1315298.sal@utas.edu.om',f'90000010'))
# add data to the treeview
   for contact in contacts:
    tree.insert('', T.END, values=contact)
   def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
   tree.bind('<<TreeviewSelect>>', item_selected)
   tree.grid(row=0, column=0, sticky='nsew')
  
# add a scrollbar
   scrollbar = ttk.Scrollbar(sb, orient=T.VERTICAL, command=tree.yview)
   tree.configure(yscroll=scrollbar.set)
   scrollbar.grid(row=0, column=1, sticky='ns')

   sb.title(" list Of Student")
   sb.mainloop()






def NT():
    path='NT'
    images=[]
    classNames=[]
    mylist=os.listdir(path)
    print(mylist)
    for cls in mylist:
      curimg=cv2.imread(f'{path}//{cls}')
      images.append(curimg)
      classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findencod(images):
      encodelist=[]
      for img in images:
        #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
      return encodelist

    def markAttendance(name):
     with open('NT.csv','r+') as f:
         mydatalist=f.readlines()
         namelist=[]
         for line in mydatalist:
             entry = line.split(',')
             namelist.append(entry[0])
         if name not in namelist:
             now=datetime.now()
             dtString=now.strftime('%H:%M:%S')
             f.writelines(f'\n{name},{dtString}')


    encodelistknown= findencod(images)
    print('Encoding complete')

    cap=cv2.VideoCapture(0)
    
    while True:
       success,img=cap.read()
       imgs=cv2.resize(img,(0,0),None,0.25,0.25)
       imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
       facesCurFrame=face_recognition.face_locations(imgs)
       encodeCurFrame= face_recognition.face_encodings(imgs,facesCurFrame)

       for encodeface,faceloc in zip(encodeCurFrame,facesCurFrame):
          matches=face_recognition.compare_faces(encodelistknown,encodeface)
          faceDis=face_recognition.face_distance(encodelistknown,encodeface)
          #print(faceDis)
          matchIndex=np.argmin(faceDis)

          if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
        
        
       cv2.waitKey(1)
       cv2.imshow('webcam',img)  
    


def T7():
            sub= Toplevel(w)
            fi=Image.open('C:\\Users\\User\\Desktop\\final_project\\last.jpg')
            re=fi.resize((1000,1000),Image.ANTIALIAS)
            b=ImageTk.PhotoImage(re)
            l=T.Label(sub,image=b)
            message = T.Label(
            sub, text="Face-Recognition-System Attendenc", fg="gray",bg="white", width=50,
            height=3, font=('times', 25, 'bold'))
            message.place(x=0, y=20)
            b11=T.Button(sub, text="List Of Student ",
                     command=N1, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b11.place(x=500,y=250)

            b21=T.Button(sub, text="attendance",
                     command=NT, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b21.place(x=500,y=350)

            
            b31=T.Button(sub, text="show attendence file",
                     command=file, fg="white", bg="gray",
                     width=30, height=2, activebackground="orange",
                     font=('times', 15, ' bold '))
            b31.place(x=500,y=450)

            b41= T.Button(sub, text="back",
                     command=sub.destroy, fg="white", bg="gray",
                     width=30, height=2, activebackground="red",
                     font=('times', 15, ' bold '))
            b41.place(x=500, y=550)
            sub.title("Attandance")
            sub.geometry('1000x1000')
            l.pack()
            sub.mainloop()

###############################################   senthel   ####################################################

def T11():
        b1=T.Button(w, text="Computer Security B",
                     command=T2 , fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b1.place(x=130,y=50)

        b2=T.Button(w, text="Network Technology",
                     command=T7, fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b2.place(x=130,y=130)
        b3=T.Button(w, text="Network Security A",
                     command=T6, fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b3.place(x=130,y=210)

        b4= T.Button(w, text="cancel",
                     command=te, fg="black", bg="white",
                     width=30, height=3, activebackground="red",
                     font=('times', 15, ' bold '))
        b4.place(x=130, y=290)

################################# Rhouma ###################################################3
        
def T21():
        b1=T.Button(w, text="Graduation Project 1",
                     command=T8, fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b1.place(x=130,y=50)

        b2=T.Button(w, text="Graduation Project 2",
                     command=T4, fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b2.place(x=130,y=130)
        b3=T.Button(w, text="Computer Security A ",
                     command=T1, fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b3.place(x=130,y=210)

        b4= T.Button(w, text="cancel",
                     command=te, fg="black", bg="white",
                     width=30, height=3, activebackground="red",
                     font=('times', 15, ' bold '))
        b4.place(x=130, y=290)
        

###################################### Mohamed ################################################
def T31():
        b1=T.Button(w, text="Innovations in Network and Security",
                     command=T5 , fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b1.place(x=130,y=50)

        b2=T.Button(w, text="Ethical Hacking and Network Defence",
                     command=T3, fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b2.place(x=130,y=130)
        b3=T.Button(w, text="cancel",
                     command=te , fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
        b3.place(x=130,y=210)

######################################### Teachers ################################

def te():
    
    b1=T.Button(w, text="Mr.Mohammed Saleem",
                     command=lambda: T31() , fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
    b1.place(x=130,y=50)

    b2=T.Button(w, text="Mr.Rhouma",
                     command=lambda: T21() , fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
    b2.place(x=130,y=130)
    b3=T.Button(w, text="Mr.Senthil Kumar",
                     command=lambda: T11(), fg="black", bg="white",
                     width=30, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
    b3.place(x=130,y=210)

    b4= T.Button(w, text="cancel",
                     command=w.destroy, fg="black", bg="white",
                     width=30, height=3, activebackground="red",
                     font=('times', 15, ' bold '))
    b4.place(x=130, y=290)




############################################# Start Button #######################################
    

b1= T.Button(w, text="Start",
                     command=te , fg="black", bg="white",
                     width=20, height=3, activebackground="gray",
                     font=('times', 15, ' bold '))
b1.place(x=400,y=270)



l.pack()
w.title("Student Attendance System")
w.geometry('1000x1000')
w.mainloop()