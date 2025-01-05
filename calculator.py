#importing tkinter module as tk
import tkinter as tk

#defining function to perform the calculations
def Calculation():
    #using error handling to handel errors
    try:
        #used to get the value entered by the user to from the entry widget
        num1=e_num1.get()
        num2=e_num2.get()
        
        #if entries are null raise error
        if not num1 or not num2:
            result_lable.config(text="Error: please enter both numbers")
            return
        
        num1=float(num1)
        num2=float(num2)
        operation=operation_var.get()

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
             result = num1 / num2  
            else :
               result_lable.config(text="Error: Can't divide by zero") #if num2 is zero raise error
               return
        else:
            result = "Invalid operation"
        result_lable.config(text=f"Result: {result:.2f}")#printing the result
    except ValueError:
        result_lable.config(text="Please enter a valid number:")

'''
Making the main window for the programme and giving the title
setting the maximum and minimum size for the application'''

root =tk.Tk()
root.title("Calculator")
root.wm_minsize(width=400,height=400)
root.wm_maxsize(width=600,height=600)

#creating lables and entry box for to enter the no given by the user
l_num1=tk.Label(root,text="Enter first number:",)
l_num1.pack(pady=5)

e_num1=tk.Entry(root)
e_num1.pack(pady=5)

l_num2=tk.Label(root,text="Enter second number:")
l_num2.pack(pady=5)

e_num2=tk.Entry(root)
e_num2.pack(pady=5)

# setting default operation value to be add
operation_var=tk.StringVar(value='add')

#creating checkboxes to select the operation to be performed
box_add=tk.Radiobutton(root,text="ADD",variable=operation_var,value="add")
box_add.pack(pady=5)

box_subtract=tk.Radiobutton(root,text="SUBTRACT",variable=operation_var,value="subtract")
box_subtract.pack(pady=5)

box_multiply=tk.Radiobutton(root,text="MULTIPLY",variable=operation_var,value="multiply")
box_multiply.pack(pady=5)

box_divide=tk.Radiobutton(root,text="DIVIDE",variable=operation_var,value="divide")
box_divide.pack(pady=5)

#creating a calculate button which send the operation to the function and function perform the operation
cal_button=tk.Button(root,text="CALCULATE",command=Calculation)
cal_button.pack(pady=5)

#making a result lable to display the result
result_lable=tk.Label(root,text="RESULT: ",)
result_lable.pack(pady=10)


#it keeps the application open until the application is closed
root.mainloop()