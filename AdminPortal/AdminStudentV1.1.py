import _tkinter
import tkinter as tk
from tkinter import ttk


def login_page():
    global username_entry, password_entry
    username_label = ttk.Label(frame, text="Username: ")
    username_entry = ttk.Entry(frame, width=50)
    password_label = ttk.Label(frame, text="Password: ")
    password_entry = ttk.Entry(frame, show="x", width=50)
    login_button = ttk.Button(frame, text="Login", width=30, command=login)
    # username_label.place(x=250, y=20)
    # username_entry.place(x=250, y=40)
    # password_label.place(x=250, y=80)
    # password_entry.place(x=250, y=100)
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack()


def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


def back_button():
    # ttk.Button(frame, text="Back", command=admin).grid(row=row, column=column)
    ttk.Button(frame, text="Back", command=admin).pack()


def login():
    if username_set == username_entry.get().lower() and password_set == password_entry.get():
        admin()

    else:
        ttk.Label(frame, text="Incorrect credentials. Please try again.").pack()


def admin():
    clear_frame()
    try:
        for i in students:
            if i.winfo_ismapped():
                i.destroy()

    except NameError:
        pass

    except _tkinter.TclError:
        pass

    finally:
        ttk.Label(frame, text="Admin Portal").pack()
        add_student_button = ttk.Button(frame, text="Add student", command=add_student_frame)
        search_student_button = ttk.Button(frame, text="Search students", command=search_student)
        view_students_button = ttk.Button(frame, text="View students", command=view_students)
        add_student_button.pack()
        search_student_button.pack()
        view_students_button.pack()


def view_students():
    global students
    students = []
    clear_frame()
    back_button()
    file = open("FrameDatabase.txt", "r")
    for line in file.readlines():
        students.append(ttk.Label(text=line.strip()))
    for i in students:
        i.pack()
    file.close()


def add_student_frame():
    global name_entry, age_entry
    clear_frame()
    name_label = ttk.Label(frame, text="Name: ")
    name_entry = ttk.Entry(frame)
    age_label = ttk.Label(frame, text="Age: ")
    age_entry = ttk.Entry(frame)
    add_button = ttk.Button(frame, text="Submit", command=check_age_int)
    back_button()
    name_label.pack()
    name_entry.pack()
    age_label.pack()
    age_entry.pack()
    add_button.pack()


def check_age_int():
    error_label = ttk.Label()
    if age_entry.get().isnumeric():
        if 0 < int(age_entry.get()) < 100:
            if not name_entry.get().isnumeric():
                if name_entry.get() != "":
                    add_student_file()

                else:
                    error_label = ttk.Label(frame, text="Name must contain something")

            else:
                error_label = ttk.Label(frame, text="Name cannot be a number")

        else:
            error_label = ttk.Label(frame, text="     Age must between 1-99     ")

    else:
        error_label = ttk.Label(frame, text="       Age must be a number       ")

    error_label.pack()


def add_student_file():
    file = open("FrameDatabase.txt", "a")
    file.write(f"{name_entry.get()}, {age_entry.get()}\n")
    file.close()
    choice()


def search_student():
    global search_entry
    clear_frame()
    back_button()
    search_label = ttk.Label(frame, text="Enter search: ")
    search_entry = ttk.Entry(frame)
    search_button = ttk.Button(frame, text="Search", command=straight_search)
    search_label.pack()
    search_entry.pack()
    search_button.pack()


def get_names():
    file = open("FrameDatabase.txt", "r+")
    data_list = []
    for line in file.readlines():
        data_list.append(line.strip().split(", "))
    return data_list


def straight_search():
    file = open("FrameDatabase.txt", "r+")
    data_list = []
    file_not_found = True
    global entry
    entry = search_entry.get()
    global data_name, data_age
    for line in file.readlines():
        data_list.append(line.strip().split(", "))
    for name_x in data_list:
        name = name_x[0]
        if entry == name:
            file_not_found = False
            data_name = name
            data_age = name_x[1]
            edit_student_frame()
    if file_not_found:
        ttk.Label(frame, text="Student not found. Please try again.").pack()


def edit_student_frame():
    clear_frame()
    global new_name_entry, new_age_entry

    file = open("FrameDatabase.txt", "r")
    data_list = []
    for line in file.readlines():
        data_list.append(line.strip())

    new_name_label = ttk.Label(frame, text="New name: ")
    new_name_entry = ttk.Entry(frame)
    new_age_label = ttk.Label(frame, text="New age: ")
    new_age_entry = ttk.Entry(frame)
    submit_button = ttk.Button(frame, text="Submit", command=edit_student)
    delete_button = ttk.Button(frame, text="Delete", command=delete_student)
    back_button()
    new_name_label.pack()
    new_name_entry.pack()
    new_age_label.pack()
    new_age_entry.pack()
    submit_button.pack()
    delete_button.pack()
    for item in data_list:
        if entry == item.split(", ")[0]:
            ttk.Label(frame, text=f"{item}").pack()
            break

    file.close()


def edit_student():
    file = open("FrameDatabase.txt", "r")
    new_lines = file.readlines()
    if new_name_entry.get() == "":
        ttk.Label(frame, text="Please fill out all details").pack()

    else:
        for i in new_lines:
            a = i.strip()
            if a.split(", ")[0] == data_name and a.split(", ")[1] == data_age:
                new_lines[new_lines.index(i)] = f"{new_name_entry.get()}, {new_age_entry.get()}"
        file.close()
        file2 = open("FrameDatabase.txt", "w")
        file2.write("")
        file2.close()
        file3 = open("FrameDatabase.txt", "a")
        for j in new_lines:
            new_lines[new_lines.index(j)] = j.strip()
        for line in new_lines:
            file3.write(f"{line}\n")
        admin()


def delete_student():
    file = open("FrameDatabase.txt", "r")
    new_lines = file.readlines()
    for i in new_lines:
        a = i.strip()
        if a.split(", ")[0] == data_name and a.split(", ")[1] == data_age:
            new_lines.remove(i)
    file.close()
    file2 = open("FrameDatabase.txt", "w")
    file2.write("")
    file2.close()
    file3 = open("FrameDatabase.txt", "a")
    for j in new_lines:
        new_lines[new_lines.index(j)] = j.strip()
    for line in new_lines:
        file3.write(f"{line}\n")
    admin()


def search():
    file = open("FrameDatabase.txt", "r+")
    index = 0
    correct_names = []
    data_list = []
    for line in file.readlines():
        data_list.append(line.strip().split(", "))
    for name_x in data_list:
        name = name_x[0]
        for letter in search_entry.get():
            if letter != name[index]:
                index = 0
                break
            index += 1
            correct_names.append(name_x)
            index = 0
            continue

    pos = 1
    search_label = ttk.Label(frame, text="Search results:")
    if search_label.winfo_ismapped():
        search_label.pack_forget()
    search_label.pack()
    for item in correct_names:
        global search_result_button
        search_result_button = ttk.Button(frame, text=f"   {item[0]}, {item[1]}   ", command=print_button)
        search_result_button.pack()
        pos += 1


def print_button():
    print(search_result_button["text"])


def choice():
    global choice_frame
    clear_frame()
    choice_label = ttk.Label(frame, text="Do you want to add another student?")
    choice_yes_button = ttk.Button(frame, text="Yes", command=choice_to_add)
    choice_no_button = ttk.Button(frame, text="No", command=admin)
    choice_label.pack()
    choice_yes_button.pack()
    choice_no_button.pack()


def choice_to_add():
    clear_frame()
    add_student_frame()


root = tk.Tk()
root.title("Admin Portal")
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()
login_page()
username_set, password_set = "admin", "admin"
tk.mainloop()
