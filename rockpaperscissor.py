#importing required module
import tkinter as tk
import random

#defined a list for rock paper scissors
All_choices=["Rock","Paper","Scissors"]

# defining a function to manage user and system choice
def Winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a tie"
    elif (user_choice=="Rock" and computer_choice=="Scissors"):
        return "You win!"
    elif (user_choice=="Scissors" and computer_choice=="Paper"):
        return "You win!"
    elif (user_choice=="Paper" and computer_choice=="Rock"):
        return "You win!"
    else:
        return "Computer wins"
         

#defining a function for bot to select a random choice
def Game(user_choice):
    computer_choice=random.choice(All_choices)
    result=Winner(user_choice,computer_choice)
    result_label.config(text=f"You choose {user_choice} ,computer choose {computer_choice}.\n\n{result}")


def game_rock():
    Game("Rock")

def game_scissors():
    Game("Scissors")

def game_paper():
    Game("Paper")

#making main window for the game
root=tk.Tk()
root.title("Rock, Paper, Scissors game")
root.wm_minsize(width=300,height=300)
root.wm_maxsize(width=500,height=500)


tk_lable=tk.Label(root,text="Choose an option:",font=("Arial",10))
tk_lable.pack(pady=5)

#making button to select options
rock_button=tk.Button(root,text="Rock",command=game_rock)
rock_button.pack(pady=5)

paper_button=tk.Button(root,text="Paper",command=game_paper)
paper_button.pack(pady=5)

scissors_button=tk.Button(root,text="Scissors",command=game_scissors)
scissors_button.pack(pady=5)

result_label=tk.Label(root,text="Choose Rock, Paper, Scissor")
result_label.pack(pady=5)


#keeps the main window open
root.mainloop()