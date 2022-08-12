import tkinter as tk
from tkinter import ttk


def login_page():
    global login_frame, username_entry, password_entry
    login_frame = tk.Frame(root)
    username_label = ttk.Label(login_frame, text="Username: ")
    username_entry = ttk.Entry(login_frame, width=50)
    password_label = ttk.Label(login_frame, text="Password: ")
    password_entry = ttk.Entry(login_frame, show="x", width=50)
    login_button = ttk.Button(login_frame, text="Login", width=30, command=login)
    # username_label.place(x=250, y=20)
    # username_entry.place(x=250, y=40)
    # password_label.place(x=250, y=80)
    # password_entry.place(x=250, y=100)
    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)
    login_button.grid(row=2, column=1)
    login_frame.grid(row=1, column=1)


def clear_frame():
   for widgets in login_frame.winfo_children():
      widgets.destroy()


def login():
    if username_set == username_entry.get().lower() and password_set == password_entry.get():
        admin()

    else:
        ttk.Label(login_frame, text="Incorrect credentials. Please try again.").grid(row=3, column=1)


def admin():
    global admin_frame
    admin_frame = tk.Frame(root)
    login_frame.pack_forget()
    admin_frame.grid(row=0, column=0)
    login_frame.destroy()
    ttk.Label(admin_frame, text="Admin Portal").pack()
    add_student_button = ttk.Button(admin_frame, text="Add student", command=add_student_frame)
    add_student_button.pack()


def add_student_frame():
    global student_frame, name_entry, age_entry
    student_frame = tk.Frame(root)
    admin_frame.pack_forget()
    student_frame.grid(row=0, column=0)
    admin_frame.destroy()
    admin_frame.destroy()
    name_label = ttk.Label(student_frame, text="Name: ")
    name_entry = ttk.Entry(student_frame)
    age_label = ttk.Label(student_frame, text="Age: ")
    age_entry = ttk.Entry(student_frame)
    add_button = ttk.Button(student_frame, text="Add student", command=check_age_int)
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    age_label.grid(row=1, column=0)
    age_entry.grid(row=1, column=1)
    add_button.grid(row=2, column=1)


def check_age_int():
    if age_entry.get().isnumeric():
        add_student_file()

    else:
        ttk.Label(student_frame, text="Age must be a number").grid(row=3, column=1)


def add_student_file():
    file = open("FrameDatabase.txt", "a")
    file.write(f"{name_entry.get()}, {age_entry.get()}\n")
    file.close()
    choice()


def choice():
    global choice_frame
    choice_frame = tk.Frame(root)
    choice_frame.place(x=0, y=0)

    choice_label = ttk.Label(text="Do you want to add another student?")
    choice_yes_button = ttk.Button(text="Yes", command=choice_to_add)
    choice_no_button = ttk.Button(text="No", command=quit)
    choice_label.grid(row=0, column=0)
    choice_yes_button.grid(row=1, column=0)
    choice_no_button.grid(row=1, column=1)


def choice_to_add():
    choice_frame.pack_forget()
    add_student_frame()


root = tk.Tk()
root.title("Admin Portal")
root.geometry("500x500")
login_page()
username_set, password_set = "admin", "admin"
root.mainloop()
