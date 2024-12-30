import random
import string

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

length=int(input("Enter the length of the password: "))
print('''Enter the complexity for the password:
         1. Letters only
         2. Letters and digits
         3. Letters,digits and symbols''')
complexity=int(input("Enter the complexity (Enter only 1,2,3): "))

My_pass=Password_Generator(length,complexity)
print(f"Your password is: {My_pass}")