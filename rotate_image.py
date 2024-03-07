import cv2  # importing cv 
import imutils 
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import glob #globbing utility.
import os
import shutil
import tkinter

root = Tk()
root.title('Rotate Images')
root.geometry('330x500')

def rotateright_onefile():
    filepath = filedialog.askopenfilename(initialdir="D:\\THEKKBox\\dev\\resize images\\test"
                                          ,title="Select File")
    # print(filepath)
    image = cv2.imread(filepath)
    Rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Rotated", Rotated_image)
    cv2.imwrite(filepath,Rotated_image)
    cv2.waitKey(0) 

def rotateright_allfile():
    path=askdirectory(title='Select your folder',
                      initialdir="D:\\THEKKBox\\dev\\resize images\\test")
    print('Path:',path + '/*')
    
    A = path + '/*'
    for file in glob.glob(A):
        # print(file)
        a = cv2.imread(file)
        # print(a)

        Rotated_image = cv2.rotate(a, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("Rotated", Rotated_image)
        cv2.imwrite(file,Rotated_image)
        cv2.waitKey(1000) #wait for 1 second
        cv2.destroyAllWindows() #destroy the window

def rotateleft_onefile():
    filepath = filedialog.askopenfilename(initialdir="D:\\THEKKBox\\dev\\resize images\\test"
                                          ,title="Select File")
    # print(filepath)
    image = cv2.imread(filepath)
    Rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Rotated", Rotated_image)
    cv2.imwrite(filepath,Rotated_image)
    cv2.waitKey(0) 

def rotateleft_allfile():
    path=askdirectory(title='Select your folder',
                      initialdir="D:\\THEKKBox\\dev\\resize images\\test")
    print('Path:',path + '/*')
    
    A = path + '/*'
    for file in glob.glob(A):
        # print(file)
        a = cv2.imread(file)
        # print(a)

        Rotated_image = cv2.rotate(a, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("Rotated", Rotated_image)
        cv2.imwrite(file,Rotated_image)
        cv2.waitKey(1000) #wait for 1 second
        cv2.destroyAllWindows() #destroy the window

def upsidedown_onefile():
    filepath = filedialog.askopenfilename(initialdir="D:\\THEKKBox\\dev\\resize images\\test"
                                          ,title="Select File")
    # print(filepath)
    image = cv2.imread(filepath)
    Rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    cv2.imshow("Rotated", Rotated_image)
    cv2.imwrite(filepath,Rotated_image)
    cv2.waitKey(0) 

def upsidedown_allfile():
    path=askdirectory(title='Select your folder',
                      initialdir="D:\\THEKKBox\\dev\\resize images\\test")
    print('Path:',path + '/*')
    
    A = path + '/*'
    for file in glob.glob(A):
        # print(file)
        a = cv2.imread(file)
        # print(a)

        Rotated_image = cv2.rotate(a, cv2.ROTATE_180)
        cv2.imshow("Rotated", Rotated_image)
        cv2.imwrite(file,Rotated_image)
        cv2.waitKey(1000) #wait for 1 second
        cv2.destroyAllWindows() #destroy the window

def flip_onefile():
    filepath = filedialog.askopenfilename(initialdir="D:\\THEKKBox\\dev\\resize images\\test"
                                          ,title="Select File")
    # print(filepath)
    image = cv2.imread(filepath)
    # Rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    Rotated_image = cv2.flip(image, 1) 
    cv2.imshow("Rotated", Rotated_image)
    cv2.imwrite(filepath,Rotated_image)
    cv2.waitKey(0) 

def flip_allfile():
    path=askdirectory(title='Select your folder',
                      initialdir="D:\\THEKKBox\\dev\\resize images\\test")
    print('Path:',path + '/*')
    
    A = path + '/*'
    for file in glob.glob(A):
        # print(file)
        a = cv2.imread(file)
        # print(a)

        # Rotated_image = cv2.rotate(a, cv2.ROTATE_180)
        Rotated_image = cv2.flip(a, 1) 
        cv2.imshow("Rotated", Rotated_image)
        cv2.imwrite(file,Rotated_image)
        cv2.waitKey(1000) #wait for 1 second
        cv2.destroyAllWindows() #destroy the window

def flipupdown_onefile():
    filepath = filedialog.askopenfilename(initialdir="D:\\THEKKBox\\dev\\resize images\\test"
                                          ,title="Select File")
    # print(filepath)
    image = cv2.imread(filepath)
    # Rotated_image = cv2.rotate(image, cv2.ROTATE_180)
    Rotated_image = cv2.flip(image, 0) 
    cv2.imshow("Rotated", Rotated_image)
    cv2.imwrite(filepath,Rotated_image)
    cv2.waitKey(0) 

def flipupdown_allfile():
    path=askdirectory(title='Select your folder',
                      initialdir="D:\\THEKKBox\\dev\\resize images\\test")
    print('Path:',path + '/*')
    
    A = path + '/*'
    for file in glob.glob(A):
        # print(file)
        a = cv2.imread(file)
        # print(a)

        # Rotated_image = cv2.rotate(a, cv2.ROTATE_180)
        Rotated_image = cv2.flip(a, 0) 
        cv2.imshow("Rotated", Rotated_image)
        cv2.imwrite(file,Rotated_image)
        cv2.waitKey(1000) #wait for 1 second
        cv2.destroyAllWindows() #destroy the window


  
# # read an image as input using OpenCV 
# image = cv2.imread(r"rotateimage.jpg") 
  
# Rotated_image = imutils.rotate(image, angle=45) 
# Rotated1_image = imutils.rotate(image, angle=90) 
  
# display the image using OpenCV of 
# angle 45 
# cv2.imshow("Rotated", Rotated_image) 
  
# display the image using OpenCV of  
# angle 90 
# cv2.imshow("Rotated", Rotated1_image) 
  
# This is used for To Keep On Displaying 
# The Image Until Any Key is Pressed 
# cv2.waitKey(0) 

button_rotate_right = Button(text="หมุนขวา",command=rotateright_onefile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="หมุนขวาทั้งโฟลเดอร์",command=rotateright_allfile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="หมุนซ้าย",command=rotateleft_onefile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="หมุนซ้ายทั้งโฟลเดอร์",command=rotateleft_allfile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="กลับหัว",command=upsidedown_onefile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="กลับหัวทั้งโฟลเดอร์",command=upsidedown_allfile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="กลับภาพซ้ายขวา",command=flip_onefile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="กลับภาพซ้ายขวาทั้งโฟลเดอร์",command=flip_allfile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="กลับภาพบนล่าง",command=flipupdown_onefile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

button_rotate_right = Button(text="กลับภาพบนล่างทั้งโฟลเดอร์",command=flipupdown_allfile)
button_rotate_right.pack(anchor=tkinter.W,padx=100,pady=10)

root.mainloop()

# cv2.imwrite("rotateimage.jpg",Rotated1_image)