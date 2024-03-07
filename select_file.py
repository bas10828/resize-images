from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\THEKKBox\\dev\\resize images\\test"
                                          ,title="Open File")
    file = open(filepath,'r')
    print(file.read())
    # print(filepath)
    file.close()

window = Tk()
window.geometry('320x320')
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()