#importing the required modules 
import tkinter as tk
from tkinter import messagebox
import random
import string

# Defining a function to generate password based on length and complexity
def Password_Generator(length,complexity):
    My_password=""

    if complexity==1:
        My_password=string.ascii_letters
    
    elif complexity==2:
        My_password=string.ascii_letters + string.digits

    elif complexity==3:
        My_password=string.ascii_letters + string.digits + string.punctuation

    else:
        print("Invalid complexity:")

    Password=''
    
    for i in range(length):
        Password+=random.choice(My_password)
    
    return Password


'''
It generates password based on user input.
Display the generated password.
It also handling the error if user enter wrong complexity.
'''

def Generate_password():
    try:
        length=int(length_entry.get())
        complexity=complexity_level.get()
        if complexity not in [1,2,3]:
            raise ValueError("Invalid complexity:")
        password=Password_Generator(length,complexity)
        result.config(text=f"{password}")
    except ValueError:
        messagebox.showerror("Error, Please enter valid complexity")


def CopyPassword():
    password=result.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied","Password copied to clipboard")
    else:
        messagebox.showerror("Error","No password to copy")


#creating a main window for the application and setting title for window
root=tk.Tk()
root.title("PASSOWRD GENERAOTR")

#setting the size of the window 
root.wm_minsize(width=300,height=300)
root.wm_maxsize(width=400,height=400)

#creating a lable and a entry box for password length
length_lable=tk.Label(root,text="Enter length: ")
length_lable.pack(pady=4)
length_entry=tk.Entry(root)
length_entry.pack(pady=4)

#creating alable and complexity selection box for selecting complexity
complexity_lable=tk.Label(root, text="Enter the complexity: ")
complexity_lable.pack(pady=4)
complexity_level=tk.IntVar()
complexity_level.set(1)#setting value of complexity of password to default 1


#creating a frame window to hold the radio button for the complexity
complexity_frame=tk.Frame(root)
complexity_frame.pack(pady=5)

#creating radio button for selecting complexity.
tk.Radiobutton(complexity_frame,text="Letters only",variable=complexity_level,value=1).pack(anchor="w")#anchor=w means radiobutton is aligned to west
tk.Radiobutton(complexity_frame,text="Letters and digits",variable=complexity_level,value=2).pack(anchor="w")
tk.Radiobutton(complexity_frame,text="Letters, digits and symbols",var=complexity_level,value=3).pack(anchor="w")

#creating a generete button to generate passowrd
Gen_button=tk.Button(root,text="GENERATE PASSOWRD",command=Generate_password)
Gen_button.pack(pady=12)

#lable button to display generated passowrd
result=tk.Label(root,text="",fg="black")
result.pack(pady=6)

#created a copy button to copy the generated password
copy_button=tk.Button(root,text="COPY PASSWORD",command=CopyPassword)
copy_button.pack(pady=5)


#this mainloop keeps the window on
root.mainloop()
