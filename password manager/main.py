from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import shutil
from os import *


root = Tk()
root.title("Password Manager")
root.geometry("200x100")
root.resizable(0,0)

def window():
    global e1
    global e2
    global f2
    global top
    top = Toplevel()
    top.geometry('300x200')
    root.withdraw()
    top.resizable(0,0)
    f2 = Frame(top)
    f2.grid(padx = 20,pady = 60)
    lbl = Label(f2,text = "Enter the title -")
    lbl.grid(row = 0,column = 0)
    e1 = Entry(f2,width = 15)
    e1.grid(row = 0,column = 1,padx = 5)
    lbl = Label(f2, text="Enter password -")
    lbl.grid(row=1, column=0)
    e2 = Entry(f2, width=15)
    e2.grid(row=1, column=1, padx=5)
    btn = Button(f2,text = "SAVE" , command = save)
    btn.grid(row = 2 ,column = 1)
    back_btn = Button(f2, text="Back to menu",command= _home)
    back_btn.grid(row=3, column=1)

def _home():
    top.withdraw()
    root.deiconify()

def save():
    global f
    title = e1.get()
    pwd = e2.get()
    f = open(title+".txt","a")
    f.write("title - "+title.capitalize()+"\n"+"Password-"+pwd)
    shutil.move(title+".txt",'data/')
    messagebox.showinfo("Info","Credentials have been saved")

def _fetch():
    root.filename = filedialog.askopenfile(initialdir = "/Users/ratish/Desktop/password manager/data")






f1 = Frame(root,width = 100 , height = 50)
f1.grid(padx = 20,pady = 20)

save_btn = Button(f1,text = "Save Password",command = window)
save_btn.grid(row = 0 , column = 1)

fetch_btn = Button(f1, text="Get saved passwords" , command = _fetch)
fetch_btn.grid(row = 1,  column = 1)






root.mainloop()

