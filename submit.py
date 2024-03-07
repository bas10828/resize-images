import tkinter
from tkinter import messagebox
root=tkinter.Tk()

def OnClick_Submit():
    name=name_textbox.get()
    email=email_textbox.get()
    messagebox.showinfo("Captured Data",name )
    print(name,email)


root.geometry("300x400")

root.title("My form")
name_label=tkinter.Label(root,text="Enter Name")
name_label.pack(anchor=tkinter.W,padx=10)
name_textbox=tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W,padx=10)

email_label=tkinter.Label(root,text="Enter Email")
email_label.pack(anchor=tkinter.W,padx=10)
email_textbox=tkinter.Entry(root)
email_textbox.pack(anchor=tkinter.W,padx=10)

submit_button=tkinter.Button(root,text='Submit',command=OnClick_Submit)
submit_button.pack(anchor=tkinter.W,padx=10)
root.mainloop()