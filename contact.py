#importing required modules
import tkinter as tk
#importing messagebox from tkinter
from tkinter import messagebox

#using a text file to save all the contacts
contact_file="contact.txt"

#function to show all contact when the programme starts
def show_contact():
    with open(contact_file,"a+") as file:#opening the file
        file.seek(0)#placing file pointer at 0 to see details from starting
        for ln in file:
            listbox.insert(tk.END,ln.strip())#entering all the saved contact into the listbox

#function to save all contact
def save_contact():
    with open(contact_file,"w") as file:
        for ln in listbox.get(0,tk.END):#getting all the contact from the listbox
            file.write(ln.strip() +"\n")#adding all contact into the file

#function to add contact
def add_contact():
    #getting required details form the entry box
    name=name_box.get()
    phone=phone_box.get()
    email=email_box.get()
    address=address_box.get()

    if name and phone:# check if name and phone number box are filled
        contact_info=f"NAME: {name}    ||    PHONE NO: {phone}    ||    EMAIL: {email}    ||    ADDRESS: {address}"
        listbox.insert(tk.END,contact_info)
        save_contact()#calling function to save contact
        clear_entries()#calling function to clear entry box
        messagebox.showinfo("SUCCESS","Contact added")
    else:
        messagebox.showerror("Please enter phone number and name")

#function to delete a contact
def delete_contact():
    selected_contact=listbox.curselection()#get the selected contact from the listbox
    if selected_contact:
        listbox.delete(selected_contact)#delete the selected contact
        save_contact()#calling sunction to save the contact
        messagebox.showinfo("SUCCESS","Contact deleted successfully:")

#function too update the selected contact
def update_contact():
    selected_contact=listbox.curselection()
    if selected_contact:
       #getting the required details to update a contact
       name=name_box.get()
       phone=phone_box.get()
       email=email_box.get()
       address=address_box.get()
       
       if name and phone:#phone no and name is required to update a contact
        contact_info=f"NAME: {name}    ||    PHONE NO: {phone}    ||    EMAIL: {email}    ||    ADDRESS: {address}"#update the contact with required details
        listbox.delete(selected_contact)
        listbox.insert(selected_contact,contact_info)
        save_contact()
        clear_entries()
        messagebox.showinfo("Success","Contact updated successfully")
       else:
           messagebox.showerror("Error","Please enter phone no and name") 
    else:
        messagebox.showerror("Error","Please select a contact to update:")

#function to search a contact in phonebook directory
def search_contact():
    search_item=search_box.get()
    search_item.lower()
    #searching if phone no or name matches the contact
    for search in listbox.get(0,tk.END):
        if search_item in search.lower():
            messagebox.showinfo("Note","Contact found")
            return
    messagebox.showerror("Note","No contact found")
    

#function to clear entries when you click on any button
def clear_entries():
    name_box.delete(0,tk.END)
    phone_box.delete(0,tk.END)
    email_box.delete(0,tk.END)
    address_box.delete(0,tk.END)
    

#creating a main window
root=tk.Tk()
root.title("CONTACT BOOK")
root.geometry("500x600")

#label for name 
label=tk.Label(root,text="Name:")
label.pack(pady=5)

#entry box to enter your name
name_box=tk.Entry(root,width=30)
name_box.pack(pady=5)

#label for phone no
phone=tk.Label(root,text="Phone No:")
phone.pack(pady=5)

#Entry box to enter phone no
phone_box=tk.Entry(root,width=30)
phone_box.pack(pady=5)

#lable for email
email_lable=tk.Label(root,text="Email:")
email_lable.pack(pady=5)

#entry box to enter the email
email_box=tk.Entry(root,width=30)
email_box.pack(pady=5)

#lable for address
address_lable=tk.Label(root,text="Address:")
address_lable.pack(pady=5)

#entry box to enter address
address_box=tk.Entry(root,width=30)
address_box.pack(pady=5)

#button to add contact
add_button=tk.Button(root,text="Add Contact",command=add_contact)
add_button.pack(pady=5)

#update button to update the changes to the selected contact
update_button=tk.Button(root,text="Update Conact",command=update_contact)
update_button.pack(pady=5)

#delete button to delete a contact
delete_button=tk.Button(root,text="Delete Contact", command=delete_contact)
delete_button.pack(pady=10)

#lable for search text
search=tk.Label(root,text="SEARCH YOUR CONACT:")
search.pack(pady=5)

#search box to enter details to search contact
search_box=tk.Entry(root,width=30)
search_box.pack(pady=5)

#search button to search a contact
search_button=tk.Button(root,text="Search",command=search_contact)
search_button.pack(pady=5)

#a listbox to display the details of the contact
listbox=tk.Listbox(root,width=50,height=10)
listbox.pack(pady=10)

#show all the saved contact detains when you open programme again
show_contact()

#keeps the main window open
root.mainloop()

