#importing required module
import tkinter as tk

task_file="Alltask.txt"#naming text file as Alltask.txt which stores all the task

#function to display all the task from the file
def show_task():
    with open(task_file,"a+") as file:
        file.seek(0)# move the file cursor to the beginning of the file
        task=file.readlines()#reading all the task from file
        for AllTask in task:
            listbox.insert(tk.END,AllTask)#inserting all the task into the checkbox

#function to add a new task 
def add_task():
    task=Entry.get()#from the entry box getting all the text 
    if task!="":#if task is not empty
        listbox.insert(tk.END,task)#add task to the listbox
        Entry.delete(0,tk.END)#clear the content in the entry box
        save_alltask()#callig save_alltask to update the task in the file


#function to save all the task of the file
def save_alltask():
    with open (task_file,"w") as file:#open file in writemode to overwrite the task to avoid repeating of task
        task=listbox.get(0,tk.END)#getting all the task from the list box
        for AllTask in task:
            file.write(AllTask + "\n")#write each task to file with proper alignments

#function to remove task
def remove_task():
    select=listbox.curselection()#This get the index of the selected task
    if select:
        listbox.delete(select)#removing the selecting task
        save_alltask()#save the updated task into the file


#making the main window
root=tk.Tk()
root.title("To-Do List")


#creating a lable for to enter task
Entry_lable=tk.Label(root,text="ENTER YOUR TASK",font=("Arial",10))
Entry_lable.pack(pady=5)

#Creating a entry box to enter your task
Entry=tk.Entry(root,width=60,font=("Arial,20"),borderwidth=6)
Entry.pack(pady=10)

#making a add button to add your task
Add_button=tk.Button(root,text="Add Task",borderwidth=4,command=add_task)
Add_button.pack(pady=10)

#creating a listbox to display all the task
listbox=tk.Listbox(root,width=40,height=10,font=("Arial",12),borderwidth=8)
listbox.pack(pady=10)

#creating a button to remove the task
remove=tk.Button(root,text="Remove Task",width=20,borderwidth=4,command=remove_task)
remove.pack(pady=5)

#shows all the task when programme starts
show_task()

#keeps open the main window 
root.mainloop()