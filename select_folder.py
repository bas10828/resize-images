from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

# path=askdirectory(title='Select your folder')
# print('Path:')
# print(path)

root = Tk()
root.title('Open Windows')
root.resizable(False,False)
root.geometry('300x150')

def Select_folder():
    path=askdirectory(title='Select your folder')
    print('Path:',path + '/*')

open_button = ttk.Button(root,text='Select your folder' ,command=Select_folder)
open_button.pack(expand=True)
root.mainloop()