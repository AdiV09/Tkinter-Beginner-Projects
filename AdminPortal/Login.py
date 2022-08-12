import tkinter as tk
from tkinter import ttk


def login():
    if username.get() == in_username and password.get() == in_password:
        print("Login successful")
        window.destroy()

    else:
        print("Incorrect. Please try again.")


in_username = "Adi"
in_password = "h"
window = tk.Tk()
window.geometry("500x500")
label_username = ttk.Label(text="Username: ")
label_password = ttk.Label(text="Password: ")
username = ttk.Entry()
password = ttk.Entry(show="*")
login_button = ttk.Button(text="Login", command=login)

label_username.place(x=25, y=25)
label_password.place(x=25, y=75)
username.place(x=50, y=50)
password.place(x=50, y=100)
login_button.place(x=25, y=125)
window.mainloop()
