#importing required module 
import tkinter as tk

#function to handle button(add text in curent which is entered in the entry box)
def button1(number):
    current=entry_box.get()#it gets the current text entered in entry box
    entry_box.delete(0,tk.END)#it clears the entry box to prevent error
    entry_box.insert(0,current+str(number)) #it insert a new number

#function to clear the entry box
def clear_box():
    entry_box.delete(0,tk.END)#clear entry box


def calculate_result():#function to calculate result
    try:
        result=eval(entry_box.get())
        entry_box.delete(0,tk.END)
        entry_box.insert(0,result)#insert result in entry box
    except Exception as e:
        entry_box.delete(0,tk.END)#clear entry box if there is an error
        entry_box.insert(0,"Error")

def handle_button(value):
    button1(value)


#first creating a main window for the application 
root=tk.Tk()
root.title("CALCULATOR")
root.wm_maxsize(width=600,height=500)

#creating entryy widget to see result and numbers
entry_box=tk.Entry(root,width=20,font=('Arial',16),borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4,pady=10)


'''We created a list of button because if we manually assign 
the numbers to each grid it is time consuming and make our code
more lengthy 
To resove this issue we will assign numbers to its correct
grid using loop'''

buttons=[
    ("7",1,0), ("8",1,1), ("9",1,2), ("+",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("-",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("*",3,3),
    ("0",4,0), ("C",4,1), ("=",4,2), ("/",4,3),
]

button_object=[]#created a list to store button object

#created a loop to assign the button to its proper grid position
for num,Row,Col in buttons:
    calc_button=tk.Button(root,text=num,width=4,height=2)
    calc_button.grid(row=Row,column=Col,pady=6)
    button_object.append((calc_button,num))#adding the button and its lable to button_object



#setting commands for the buttons
for button,text in button_object:
    if text=="C":
        button.config(command=clear_box)
    elif text=="=":
        button.config(command=calculate_result)
    else:
        button.config(command=lambda value=text: handle_button(value))#it passes the correct number/operation to button1 function

'''here i use lambda because it create a anonymous function(a function without name)
.Button generally dont accept the arguments but using lambda function we can
pass arguments to the function.
It assign the button value to value varible and then send it to handel_button'''


#keeps the main window on
root.mainloop()
