from tkinter import * 
from tkinter import ttk 
import random
import time 
from main import * 
from tkinter import messagebox


pinnumber = 0


def menu():
    print("----------------------------------------------------------------")
    print("1. Check account balance")
    print("2. Deposit funds ")
    print("3. Withdraw funds")
    print("4. Create account")
    print("5. Delete an account")
    print("6. Modify account details")
    print("7. Menu")

print("Hello! Welcome to Z Banking!")
menu()
''' 
If software was only command line
userInput = int(input("What would you like to do?: ")).
if userInput == 4:
    name = input("Enter your name: ")
    pinnumber = input("Please make a personal pin")
    amount = 0
    insert_new_account()
    
    elif userInput == 7:
        menu()  

    elif userInput == 1: 
        pinnumber == int(input"Please enter your pin number: ")
        for numbers in pinnumber:
            pinnumber += 1
        if pinnumber = 4:
            print(f"You have {amount} in your bank account ")
'''
#GUI ----------------------------------------------------------------

ws = Tk()
ws.title("Z Banking Information")

Label(ws, text = "Banking Information", font=f).grid(row=0,stiky=N,pady=10)
Label(ws, text = "The most secure banking app you've ever used", font=f).grid(row=1,stiky=N,)

#Functions 

def register():
    #register screen 
    register_screen = Toplevel(ws)
    register_screen.title("Register")

    Label(register_screen, text = "Please enter your detials below to register", font=f).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text = "Name", font=f).grid(row=1,sticky=W,)
    Label(register_screen, text = "Pinnumber", font=f).grid(row=2,sticky=W,)

    #Entries 
    Entry(regiser_screen).grid(row=1, column=0)
    Entry(regiser_screen).grid(row=2, column=0)

#Buttons
register_btn = Button(
    f1, 
    text='Register',
    bg='#C2BB00',
    command=register,
    font=f
)
update_btn = Button(
    f1, 
    text='Update Balance',
    bg='#C2BB00',
    command=update_amount,
    font=f
 )

login_btn = Button(
    f1, 
    text='Login',
    bg='#C2BB00',
    font=f
)

ws.mainloop()
