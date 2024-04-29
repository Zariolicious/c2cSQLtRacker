from tkinter import * 
from tkinter import ttk 
import random
import time 
from main import * 
from tkinter import messagebox


pinnumber = 0

#GUI ----------------------------------------------------------------

ws = Tk()
ws.title("Z Banking Information")

Label(ws, text = "Banking Information", font=f).grid(row=0,stiky=N,pady=10)
Label(ws, text = "The most secure banking app you've ever used", font=f).grid(row=1,stiky=N,)

#Functions 

def finish_reg(): 
    insert_new_account(temp_name, 0, temp_id, temp_pinnumber)
    print(f"Account created for {temp_name}")

def login_user(): 
    all_accounts = #make list of all accounts through the names

    #for name in all_accounts:
        #if name == temp_login_name:
        #bring to screen for withdrawing or depositing money into account 

def register():
    #Variables global allows to be used in other functions
    global temp_name
    global temp_pinnumber
    global temp_id
    temp_name = StringVar()
    temp_pinnumber = StringVar()
    temp_id = StringVar()

    #register screen 
    register_screen = Toplevel(ws)
    register_screen.title("Register")

    Label(register_screen, text = "Please enter your detials below to register", font=f).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text = "Name", font=f).grid(row=1,sticky=W,)
    Label(register_screen, text = "Pinnumber", font=f).grid(row=2,sticky=W,)
    Label(register_screen, text = "Unique ID", font=f).grid(row=3,sticky=W,)

    #Entries for user to input info for login
    Entry(regiser_screen,textvarible=temp_name).grid(row=1, column=0)
    Entry(regiser_screen,textvarible=temp_pinnumber).grid(row=2, column=0)
    Entry(regiser_screen,textvarible=temp_id).grid(row=3, column=0)

    #Buttons
    register_btn = Button(
        register_screen, 
        text='Register',
        bg='#C2BB00',
        command=register,
        font=f
    )
    update_btn = Button(
        register_screen, 
        text='Update Balance',
        bg='#C2BB00',
        command=update_amount,
        font=f
     )

def login():
    #Vars
    global temp_login_name
    global temp_login_pinnumber
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_pinnumber = StringVar()

    login_screen = Toplevel(master)
    login_screen.title("Login")

    Label(login_screen, text = "Please enter your detials below to login", font=f).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text = "Name", font=f).grid(row=1,sticky=W,)
    Label(login_screen, text = "Pinnumber", font=f).grid(row=2,sticky=W,)

    login_notif = Label(login_screen, font=f,)
    login_notif.grid(row=4,sticky=N,pady=10)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_pinnumber).grid(row=2, column=1, padx=5) 
    #Button 
    login_btn = Button(
    f1, 
    text='Login',
    command=login_user,
    bg='#C2BB00',
    font=f
).grid(row=3, sticky=W, pady=5, padx=5)

ws.mainloop()
