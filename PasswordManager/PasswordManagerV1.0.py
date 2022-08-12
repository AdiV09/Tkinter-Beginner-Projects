import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import *
from random import choice


def clear_window():
    for i in root.winfo_children():
        i.destroy()


def login_page():
    global username_entry, password_entry, username, password
    clear_window()
    username_label = Label(root, text="Username: ")
    username_entry = Entry(root)
    password_label = Label(root, text="Password: ")
    password_entry = Entry(root, show="x")
    login_button = Button(root, text="Login", command=login)
    signup_button = Button(root, text="Sign up", command=signup)
    username_label.place(x=150, y=10)
    username_entry.place(x=215, y=10)
    password_label.place(x=150, y=50)
    password_entry.place(x=215, y=50)
    login_button.place(x=160, y=80)
    signup_button.place(x=260, y=80)


def login_back_button():
    Button(root, text="Back", command=login_page).place(x=25, y=10)


def login():
    if check_user_exists(username_entry.get()):
        file = open(rf"Accounts\{username_entry.get()}.txt", "r")
        lines = file.readlines()
        if lines[0].strip().split(": ")[1] == password_entry.get():
            global login_username, login_password
            login_username, login_password = username_entry.get(), password_entry.get()
            account_page()
        else:
            showerror("Login Error", "Your password does not match")
    else:
        showerror("Login Error", f"The account '{username_entry.get()}' does not exist")


def check_user_exists(user):
    file = open("People.txt", "r")
    count = 0
    for i in file.readlines():
        if i.strip() == user:
            file.close()
            return True
        else:
            count += 1
    file.close()
    return False


def signup():
    global new_username_entry, new_password_entry
    clear_window()
    login_back_button()
    new_username_label = Label(root, text="Set username: ")
    new_username_entry = Entry(root)
    new_password_label = Label(root, text="Set password: ")
    new_password_entry = Entry(root, show="x")
    new_signup_button = Button(root, text="Sign up", command=add_user)
    new_username_label.place(x=135, y=10)
    new_username_entry.place(x=225, y=10)
    new_password_label.place(x=135, y=50)
    new_password_entry.place(x=225, y=50)
    new_signup_button.place(x=200, y=80)


def add_user():
    if check_user_exists(new_username_entry.get()):
        showerror("Signup Error", "User already exists")

    elif not password_criteria(new_password_entry.get())[0]:
        showwarning(password_criteria(new_password_entry.get())[1], password_criteria(new_password_entry.get())[2])

    elif new_username_entry.get() == "":
        showerror("Signup Error", "Please enter a username")

    else:
        file = open("People.txt", "a")
        file.write(f"{new_username_entry.get()}\n")
        file.close()
        file2 = open(rf"Accounts\{new_username_entry.get()}.txt", "a")
        file2.write(f"Login password: {new_password_entry.get()}\n")
        file2.close()
        login_page()
        showinfo("Signup Successful", "Your account has been created")


def account_page():
    global account_details
    clear_window()
    account_details = rf"Accounts\{login_username}.txt"
    account_title_label = Label(root, text="Homepage")
    view_password_button = Button(root, text="View passwords", command=view_passwords)
    add_password_button = Button (root, text="Add password", command=add_password_page)
    edit_password_button = Button(root, text="Edit password", command=search_password_page)
    account_title_label.place(x=205, y=10)
    view_password_button.place(x=190, y=30)
    add_password_button.place(x=193, y=60)
    edit_password_button.place(x=193, y=90)


def account_back_button():
    Button(root, text="Back", command=account_page).place(x=25, y=10)


def view_passwords():
    clear_window()
    account_back_button()
    file = open(account_details, "r")
    lines = file.readlines()
    for i in lines:
        Label(root, text=i.strip()).pack()


def add_password_page():
    global add_title_entry, add_password_entry
    clear_window()
    account_back_button()
    title_prompt_label = Label(root, text="Title: ")
    add_title_entry = Entry(root)
    password_prompt_label = Label(root, text="Password: ")
    add_password_entry = Entry(root, show="x")
    add_password_button = Button(root, text="Add password", command=add_password)
    random_password_button = Button(root, text="Generate password", command=check_not_null)
    title_prompt_label.place(x=175, y=10)
    add_title_entry.place(x=210, y=10)
    password_prompt_label.place(x=145, y=50)
    add_password_entry.place(x=210, y=50)
    add_password_button.place(x=150, y=80)
    random_password_button.place(x=250, y=80)


def password_criteria(check_password):
    special_chars = r"!,@#$%^&*():<>?\/"
    special_check = False
    num_check = False
    upper_check = False
    for char in check_password:
        if char in special_chars:
            special_check = True

        if char.isnumeric():
            num_check = True

        if char.isupper():
            upper_check = True

    if special_check and num_check and upper_check and len(check_password) >= 8:
        return True, None, None

    else:
        return False, "Password too weak", "Your password should be at least 8 characters long and contain" \
                                           " at least 1 special character, number and capital letter."


def add_password():
    check = password_criteria(add_password_entry.get())
    if check[0]:
        file = open(account_details, "a")
        file.write(f"{add_title_entry.get()} password: {add_password_entry.get()}\n")
        file.close()
        account_page()
        showinfo("Command successful", "Your password has been added")
    else:
        showwarning(check[1], check[2])


def check_not_null():
    global title
    title = add_title_entry.get()
    if title == "":
        showerror("Random Password Inaccessible", "Please enter your password title")
    else:
        random_password_page()


def random_password_page():
    global random_password
    clear_window()
    account_back_button()
    random_password = random_password_generate()
    Label(root, text=random_password).place(x=220, y=20)
    Button(root, text="Accept", command=add_random_password).place(x=225, y=50)
    Button(root, text="Scramble", command=random_password_page).place(x=225, y=80)


def random_password_generate():
    bank = r"abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*())_+={}[]:;<>?\/"
    random_password_ = ""
    while not password_criteria(random_password_)[0]:
        random_password_ = ""
        for i in range(12):
            random_password_ += choice(bank)
    return random_password_


def add_random_password():
    file = open(account_details, "a")
    file.write(f"{title} password: {random_password}\n")
    file.close()
    account_page()
    showinfo("Command successful", "Your password has been added")


def search_password_page():
    clear_window()
    global search_entry
    search_label = Label(root, text="Password title: ")
    search_entry = Entry(root)
    search_button = Button(root, text="Search", command=search_password_title)
    search_label.place(x=150, y=20)
    search_entry.place(x=240, y=20)
    search_button.place(x=210, y=50)


def search_password_title():
    global search
    file = open(account_details, "r")
    lines = file.readlines()
    exists = False
    search = search_entry.get()
    for i in lines:
        if i.strip().split(" password: ")[0] == search:
            exists = True
            edit_password_page()

    if not exists:
        showerror("Search Error", "No such password title")


def edit_password_page():
    clear_window()
    global edit_title_entry, edit_password_entry
    edit_title_label = Label(root, text="New title: ")
    edit_title_entry = Entry(root)
    edit_password_label = Label(root, text="New password: ")
    edit_password_entry = Entry(root)
    edit_button = Button(root, text="Edit", command=check_edit_password)
    edit_title_label.place(x=150, y=20)
    edit_title_entry.place(x=240, y=20)
    edit_password_label.place(x=150, y=50)
    edit_password_entry.place(x=240, y=50)
    edit_button.place(x=210, y=80)


def check_edit_password():
    if password_criteria(edit_password_entry.get())[0]:
        edit_password()

    else:
        showwarning(password_criteria(edit_password_entry.get())[1], password_criteria(edit_password_entry.get())[2])


def edit_password():
    file = open(account_details, "r")
    lines = file.readlines()
    count = 0
    file.close()
    file2 = open(account_details, "w")
    file2.write("")
    file2.close()
    file3 = open(account_details, "a")
    to_edit_title = edit_title_entry.get()
    to_edit_password = edit_password_entry.get()
    if to_edit_title == "":
        to_edit_title = search

    for i in lines:
        if i.strip().split("password: ")[0].strip(" ") == search:
            file3.write(f"{to_edit_title} password: {to_edit_password}\n")

        else:
            file3.write(i)
        count += 1

    file3.close()
    account_page()
    showinfo("Edit successful", "Your password has been successfully edited")


root = tk.Tk()
root.title("Password Manager")
root.geometry("500x500")
# Button(image=image).pack()
login_page()
root.mainloop()
