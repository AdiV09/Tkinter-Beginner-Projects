import tkinter as tk


def login():
    if username.get().lower() == in_username and password.get() == in_password:
        print("Login successful")
        admin_portal()
        window.destroy()

    else:
        incorrect = tk.Label(window, text="Incorrect. Please try again.")
        incorrect.place(x=10, y=165)


def admin_portal():
    global admin
    admin = tk.Tk()
    admin.geometry("250x250")
    tk.Label(admin, text="Admin Portal").pack()
    quit_button = tk.Button(admin, text="Quit", command=quit)
    quit_button.place(x=10, y=220)
    add_student_button = tk.Button(admin, text="Add student", command=close_admin)
    add_student_button.place(x=60, y=220)

def close_admin():
    admin.destroy()
    add_student()


def close_choice():
    choice_win.destroy()
    add_student()


def add_student():
    global student
    student = tk.Tk()
    student.geometry("200x200")
    tk.Label(student, text="Add student").place(x=10, y=10)
    tk.Label(student, text="Name:").place(x=15, y=45)
    global name, age
    name = tk.Entry(student)
    name.place(x=20, y=65)
    tk.Label(student, text="Age:").place(x=15, y=95)
    age = tk.Entry(student)
    age.place(x=20, y=115)
    tk.Button(student, text="Submit", command=submit).place(x=40, y=155)
    tk.Button(student, text="Cancel", command=cancel).place(x=100, y=155)


def cancel():
    student.destroy()
    admin_portal()


def submit():
    file = open("Database.txt", "a")
    file.write(f"{name.get()}, {age.get()}\n")
    file.close()
    student.destroy()
    choice()


def choice():
    global choice_win
    choice_win = tk.Tk()
    choice_win.geometry("225x125")
    tk.Label(choice_win, text="Do you want to add another student?").pack()
    tk.Button(choice_win, text="Yes", command=close_choice).place(x=50, y=50)
    tk.Button(choice_win, text="No", command=quit).place(x=140, y=50)


in_username = "admin"
in_password = "admin"
window = tk.Tk()
window.geometry("200x200")
label_username = tk.Label(window, text="Username: ")
label_password = tk.Label(window, text="Password: ")
username = tk.Entry(window)
password = tk.Entry(window, show="*")
login_button = tk.Button(window, text="Login", command=login)

label_username.place(x=10, y=15)
label_password.place(x=10, y=75)
username.place(x=20, y=40)
password.place(x=20, y=100)
login_button.place(x=10, y=130)
window.mainloop()