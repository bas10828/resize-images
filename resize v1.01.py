from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

import tkinter
import os
import shutil
import cv2 #import the library opencv
import glob #globbing utility.

root = Tk()
root.title('Resize Images')
root.resizable(False,False)
root.geometry('500x200')

def Select_folder():
    height = ""
    width = ""

    height_text = height_textbox.get()
    width_text = width_textbox.get()

    if (height_text == "") or (width_text == "") :     
        height = 252
        width = 189
        print(f'from if \n h : {height}  w : {width}')
    else:
        height = int(height_text)
        width = int(width_text)
        print(f'from else \n h : {height}  w : {width}')

    print("height : ",height)
    print("width : ",width)

    path = askdirectory(title='Select your folder')
    print('Path:',path + '/*')

    A = path + '/*'
    for file in glob.glob(A):
        print(file)
        a = cv2.imread(file)
        print(a)

        #conversion numpy array into rgb image to show
        b = cv2.resize(a,(width,height))
        cv2.imshow('show image', b)
        cv2.imwrite(file,b)
        k = cv2.waitKey(1000) #wait for 1 second
        cv2.destroyAllWindows() #destroy the window

    
    
aleat_label=tkinter.Label(root,text="คำเตือน!!! การเปลี่ยนขนาดจะเป็นการเขียนทันไฟล์ที่เลือก จงสำรองไฟล์รูปเก็บไว้ก่อนกดรันโปรแกรม" )
aleat_label.pack(anchor=tkinter.W,padx=10)
width_label=tkinter.Label(root,text="กว้างxสูง ตั้ง=189x252 นอน=252x189 px" )
width_label.pack(anchor=tkinter.W,padx=10)
width_label=tkinter.Label(root,text="Enter width(ความกว้าง)")
width_label.pack(anchor=tkinter.W,padx=10)
width_textbox=tkinter.Entry(root)
width_textbox.pack(anchor=tkinter.W,padx=10)

height_label=tkinter.Label(root,text="Enter height(ความยาว)")
height_label.pack(anchor=tkinter.W,padx=10)
height_textbox=tkinter.Entry(root)
height_textbox.pack(anchor=tkinter.W,padx=10)    

open_button = ttk.Button(root,text='Select your folder and run program' ,command=Select_folder)
open_button.pack(expand=True)
root.mainloop()