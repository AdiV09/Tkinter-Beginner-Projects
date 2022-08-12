import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3 as sql
from PIL import ImageTk, Image


def clear_window():
    for i in root.winfo_children():
        i.destroy()


def back_button():
    back = Button(root, text="Back", command=homepage)
    back.place(x=10, y=10)


def login_page():
    global username_entry, password_entry, username, password
    clear_window()
    username_label = Label(root, text="Username: ", background="#faf9ed")
    username_entry = Entry(root)
    password_label = Label(root, text="Password: ", background="#faf9ed")
    password_entry = Entry(root, show="x")
    login_button = Button(root, text="Login", command=check_admin)
    signup_button = Button(root, text="Sign up", command=signup)
    username_label.place(x=200, y=10)
    username_entry.place(x=265, y=10)
    password_label.place(x=200, y=50)
    password_entry.place(x=265, y=50)
    login_button.place(x=210, y=80)
    signup_button.place(x=310, y=80)


def check_user_exists(user_name):
    with open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Users.txt", "r") as file:
        for i in file.readlines():
            if i.strip().split(":")[0] == user_name:
                return True
        return False


def check_admin():
    if username_entry.get().lower() == "admin" and password_entry.get() == "admin":
        pass

    else:
        login()


def login():
    if username_entry.get() == "" or password_entry.get() == "":
        showerror("Login Error", "Please fill out both fields")
        return None

    if check_user_exists(f"{username_entry.get()[0].upper()}{username_entry.get()[1:].lower()}"):
        global table
        table = f"{username_entry.get().lower()}_basket"
        file = open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Users.txt", "r")
        for i in file.readlines():
            if i.strip().split(":")[1] == password_entry.get():
                homepage()
                return None
        
        showerror("Login Error", "Your password does not match")
        
    else:
        showerror("Login Error", "User does not exist")


def login_back_button():
    Button(root, text="Back", command=login_page).place(x=25, y=10)


def signup():
    global new_username_entry, new_password_entry
    clear_window()
    login_back_button()
    new_username_label = Label(root, text="Set username: ", background="#faf9ed")
    new_username_entry = Entry(root)
    new_password_label = Label(root, text="Set password: ", background="#faf9ed")
    new_password_entry = Entry(root, show="x")
    new_signup_button = Button(root, text="Sign up", command=add_user)
    new_username_label.place(x=185, y=10)
    new_username_entry.place(x=275, y=10)
    new_password_label.place(x=185, y=50)
    new_password_entry.place(x=275, y=50)
    new_signup_button.place(x=250, y=80)


def add_user():
    if check_user_exists(new_username_entry.get()):
        showerror("Signup Error", "User already exists")

    elif new_username_entry.get() == "" or new_password_entry.get() == "":
        showerror("Signup Error", "Please fill out both fields")

    elif new_username_entry.get().lower() == "admin" or new_password_entry.get() == "admin":
        showerror("Signup Error", r"Please choose a different username/password")

    else:
        format_username = f"{new_username_entry.get()[0].upper()}{new_username_entry.get()[1:].lower()}"
        file = open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Users.txt", "a")
        file.write(f"{format_username}:{new_password_entry.get()}\n")
        supermarket_db.execute(f"CREATE TABLE {new_username_entry.get().lower()}_basket (ID INTEGER PRIMARY "
                               f"KEY, ITEM TEXT, PRICE"
                               f" DECIMAL, QUANTITY INTEGER)")
        login_page()
        showinfo("Signup Successful", "Your account has been created")


def search_basket():
    global basket_photo, search_entry
    search_entry = Entry(root, width=30)
    basket_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\shopping-cart.png"))
    basket = Button(root, image=basket_photo, command=show_basket)
    basket.place(x=540, y=10)
    search_button = Button(root, text="Search", command=search_item)
    search_entry.place(x=150, y=10)
    search_button.place(x=350, y=10)


def homepage():
    clear_window()
    search_basket()
    width = 13

    category_label = Label(root, text="Categories", width=width, background="#faf9ed")
    bakery_button = tk.Button(root, text="Bakery", bg="#038f28", width=width, command=show_bakery)
    fruits_button = tk.Button(root, text="Fruits", bg="#038f28", width=width, command=show_fruits)
    veg_button = tk.Button(root, text="Veggies", bg="#038f28", width=width, command=show_vegetables)
    featuring_label = Label(root, text="Featured today: ", background="#faf9ed")
    #
    # featuring_label.place(x=175, y=70)
    category_label.place(x=10, y=100)
    fruits_button.place(x=10, y=125)
    veg_button.place(x=10, y=150)
    bakery_button.place(x=10, y=176)


def get_price(item):
    cursor = supermarket_db.execute(f"SELECT PRICE FROM ITEMS WHERE ITEM IS '{item.upper()}'")
    prices = []
    for i in cursor:
        prices.append(i[0])
    return prices[0]


def show_fruits():
    clear_window()
    homepage()
    back_button()
    global apple_photo, banana_photo, quantity_spinbox_apple, quantity_spinbox_banana
    apple_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                r"Images\apple.png"))
    image_label_apple = Label(root, image=apple_photo)
    item_label_apple = Label(root, text=f"Apple:   ${get_price('Apple')}", background="#faf9ed")
    quantity_label_apple = Label(root, text="Qty: ", background="#faf9ed")
    quantity_spinbox_apple = Spinbox(root, from_=1, to=15, wrap=True, width=10)
    x, y = 200, 100
    image_label_apple.place(x=x, y=y)
    item_label_apple.place(x=x + 5, y=y + 80)
    quantity_label_apple.place(x=x - 23, y=y + 100)
    quantity_spinbox_apple.place(x=x + 5, y=y + 100)

    banana_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\banana.png"))
    image_label_banana = Label(root, image=banana_photo)
    item_label_banana = Label(root, text=f"Banana:   ${get_price('Banana')}", background="#faf9ed")
    quantity_label_banana = Label(root, text="Qty: ", background="#faf9ed")
    quantity_spinbox_banana = Spinbox(root, from_=1, to=15, wrap=True, width=10)
    x = 370
    image_label_banana.place(x=x, y=y)
    item_label_banana.place(x=x, y=y + 80)
    quantity_label_banana.place(x=x - 23, y=y + 100)
    quantity_spinbox_banana.place(x=x + 5, y=y + 100)
    add_button = tk.Button(root, text="Add to basket", width=20, command=add_items_fruits)
    add_button.config(height=2, bg="#99ab93")
    add_button.place(x=400, y=500)


def show_vegetables():
    clear_window()
    homepage()
    back_button()
    global carrot_photo, potato_photo, quantity_spinbox_carrot, quantity_spinbox_potato
    carrot_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\carrot.png"))
    image_label_carrot = Label(root, image=carrot_photo)
    item_label_carrot = Label(root, text=f"Carrot:   ${get_price('Carrot')}", background="#faf9ed")
    quantity_label_carrot = Label(root, text="Qty: ", background="#faf9ed")
    quantity_spinbox_carrot = Spinbox(root, from_=1, to=15, wrap=True, width=10)
    x, y = 200, 100
    image_label_carrot.place(x=x, y=y)
    item_label_carrot.place(x=x + 5, y=y + 80)
    quantity_label_carrot.place(x=x - 23, y=y + 100)
    quantity_spinbox_carrot.place(x=x + 5, y=y + 100)

    potato_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\potato.png"))
    image_label_potato = Label(root, image=potato_photo)
    item_label_potato = Label(root, text=f"Potato:   ${get_price('Potato')}", background="#faf9ed")
    quantity_label_potato = Label(root, text="Qty: ", background="#faf9ed")
    quantity_spinbox_potato = Spinbox(root, from_=1, to=15, wrap=True, width=10)
    x = 370
    image_label_potato.place(x=x, y=y)
    item_label_potato.place(x=x, y=y + 80)
    quantity_label_potato.place(x=x - 23, y=y + 100)
    quantity_spinbox_potato.place(x=x + 5, y=y + 100)
    add_button = tk.Button(root, text="Add to basket", width=20, command=add_items_vegetables)
    add_button.config(height=2, bg="#99ab93")
    add_button.place(x=400, y=500)


def show_bakery():
    clear_window()
    homepage()
    back_button()
    global bread_photo, cake_photo, quantity_spinbox_bread, quantity_spinbox_cake
    bread_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                r"Images\bread.png"))
    image_label_bread = Label(root, image=bread_photo)
    item_label_bread = Label(root, text=f"Bread:   ${get_price('Bread')}", background="#faf9ed")
    quantity_label_bread = Label(root, text="Qty: ", background="#faf9ed")
    quantity_spinbox_bread = Spinbox(root, from_=1, to=15, wrap=True, width=10)
    x, y = 200, 100
    image_label_bread.place(x=x, y=y)
    item_label_bread.place(x=x + 5, y=y + 80)
    quantity_label_bread.place(x=x - 23, y=y + 100)
    quantity_spinbox_bread.place(x=x + 5, y=y + 100)

    cake_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                               r"Images\cake.png"))
    image_label_cake = Label(root, image=cake_photo)
    item_label_cake = Label(root, text=f"Cake:   ${get_price('Cake')}", background="#faf9ed")
    quantity_label_cake = Label(root, text="Qty: ", background="#faf9ed")
    quantity_spinbox_cake = Spinbox(root, from_=1, to=15, wrap=True, width=10)
    x = 370
    image_label_cake.place(x=x, y=y)
    item_label_cake.place(x=x, y=y + 80)
    quantity_label_cake.place(x=x - 23, y=y + 100)
    quantity_spinbox_cake.place(x=x + 5, y=y + 100)
    add_button = tk.Button(root, text="Add to basket", width=20, command=add_items_bakery)
    add_button.config(height=2, bg="#99ab93")
    add_button.place(x=400, y=500)


def add_items_fruits():
    apple_check = False
    apple_results = []
    if quantity_spinbox_apple.get() != "":
        if not quantity_spinbox_apple.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")
            return None

        elif int(quantity_spinbox_apple.get()) <= 0 or int(quantity_spinbox_apple.get()) > 15:
            showerror("Add Item Error", "Please ensure your quantities are more than 0 and less than 15")
            return None

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = 'Apple')"):
                if i[0] == 1:
                    apple_check = True

        if apple_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = 'Apple'")
            for i in cursor:
                apple_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{apple_results[0][0] + (get_price('Apple') * int(quantity_spinbox_apple.get()))}, "
                                   f"quantity = {apple_results[0][1] + int(quantity_spinbox_apple.get())} "
                                   f"where item == 'Apple'")

        else:
            price = int(quantity_spinbox_apple.get()) * get_price('Apple')
            quantity = quantity_spinbox_apple.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('Apple', {price}, {quantity})")

    banana_check = False
    banana_results = []
    if quantity_spinbox_banana.get() != "":
        if not quantity_spinbox_banana.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        elif int(quantity_spinbox_banana.get()) <= 0 or int(quantity_spinbox_banana.get()) > 15:
            showerror("Add Item Error", "Please ensure your quantities are more than 0 and less than 15")
            return None

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = 'Banana')"):
                if i[0] == 1:
                    banana_check = True

        if banana_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = 'Banana'")
            for i in cursor:
                banana_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{banana_results[0][0] + (get_price('Banana') * int(quantity_spinbox_banana.get()))}"
                                   f", "
                                   f" quantity = {banana_results[0][1] + int(quantity_spinbox_banana.get())} "
                                   f"where item == 'Banana'")

        else:
            price = int(quantity_spinbox_banana.get()) * get_price('Banana')
            quantity = quantity_spinbox_banana.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('Banana', {price}, {quantity})")

    supermarket_db.commit()
    showinfo("Item(s) added", "The item(s) has/have successfully been added")
    show_fruits()


def add_items_vegetables():
    carrot_check = False
    carrot_results = []
    if quantity_spinbox_carrot.get() != "":
        if not quantity_spinbox_carrot.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        elif int(quantity_spinbox_carrot.get()) <= 0 or int(quantity_spinbox_carrot.get()) > 15:
            showerror("Add Item Error", "Please ensure your quantities are more than 0 and less than 15")
            return None

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = 'Carrot')"):
                if i[0] == 1:
                    carrot_check = True

        if carrot_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = 'Carrot'")
            for i in cursor:
                carrot_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{carrot_results[0][0] + (get_price('Carrot') * int(quantity_spinbox_carrot.get()))},"
                                   f" quantity = {carrot_results[0][1] + int(quantity_spinbox_carrot.get())} "
                                   f"where item == 'Carrot'")

        else:
            price = int(quantity_spinbox_carrot.get()) * get_price('Carrot')
            quantity = quantity_spinbox_carrot.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('Carrot', {price}, {quantity})")

    potato_check = False
    potato_results = []
    if quantity_spinbox_potato.get() != "":
        if not quantity_spinbox_potato.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")
            return None

        elif int(quantity_spinbox_potato.get()) <= 0 or int(quantity_spinbox_potato.get()) > 15:
            showerror("Add Item Error", "Please ensure your quantities are more than 0 and less than 15")
            return None

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = 'Potato')"):
                if i[0] == 1:
                    potato_check = True

        if potato_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = 'Potato'")
            for i in cursor:
                potato_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{potato_results[0][0] + (get_price('Potato') * int(quantity_spinbox_potato.get()))},"
                                   f" quantity = {potato_results[0][1] + int(quantity_spinbox_potato.get())} "
                                   f"where item == 'Potato'")

        else:
            price = int(quantity_spinbox_potato.get()) * get_price('Potato')
            quantity = quantity_spinbox_potato.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('Potato', {price}, {quantity})")

    supermarket_db.commit()
    showinfo("Item(s) added", "The item(s) has/have successfully been added")
    show_vegetables()


def add_items_bakery():
    bread_check = False
    bread_results = []
    if quantity_spinbox_bread.get() != "":
        if not quantity_spinbox_bread.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")
            return None

        elif int(quantity_spinbox_bread.get()) <= 0 or int(quantity_spinbox_bread.get()) > 15:
            showerror("Add Item Error", "Please ensure your quantities are more than 0 and less than 15")
            return None

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = 'Bread')"):
                if i[0] == 1:
                    bread_check = True

        if bread_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = 'Bread'")
            for i in cursor:
                bread_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{bread_results[0][0] + (get_price('Bread') * int(quantity_spinbox_bread.get()))}, "
                                   f"quantity = {bread_results[0][1] + int(quantity_spinbox_bread.get())} "
                                   f"where item == 'Bread'")

        else:
            price = int(quantity_spinbox_bread.get()) * get_price('Bread')
            quantity = quantity_spinbox_bread.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('Bread', {price}, {quantity})")

    cake_check = False
    cake_results = []
    if quantity_spinbox_cake.get() != "":
        if not quantity_spinbox_cake.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        elif int(quantity_spinbox_cake.get()) <= 0 or int(quantity_spinbox_cake.get()) > 15:
            showerror("Add Item Error", "Please ensure your quantities are more than 0 and less than 15")
            return None

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = 'Cake')"):
                if i[0] == 1:
                    cake_check = True

        if cake_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = 'Cake'")
            for i in cursor:
                cake_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{cake_results[0][0] + (get_price('Cake') * int(quantity_spinbox_cake.get()))}, "
                                   f"quantity = {cake_results[0][1] + int(quantity_spinbox_cake.get())} "
                                   f"where item == 'Cake'")

        else:
            price = int(quantity_spinbox_cake.get()) * get_price('Cake')
            quantity = quantity_spinbox_cake.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('Cake', {price}, {quantity})")

    supermarket_db.commit()
    showinfo("Item(s) added", "The item(s) has/have successfully been added")
    show_bakery()


def show_basket():
    clear_window()
    back_button()
    cursor = supermarket_db.execute(f"SELECT * FROM {table}")
    x, y = 250, 100
    price = 0.0
    # images = []
    for i in cursor:
        price += round(i[2], 2)
        # small_img = ImageTk.PhotoImage(Image.open(fr"C:\Users\adi09\PycharmProjects\TKinter\Super"
        #                                           fr"market\SupermarketImages\small_{i[1].lower()}.png"))
        # img_label = Label(root, image=small_img)
        # images.append(img_label)
        item_button = Label(root, text=f"{i[1]} x {i[3]}        ${round(i[2], 2)}", background="#faf9ed")
        item_button.place(x=x + 40, y=y + 10)
        y += 40
    Label(root, text=f"Total:     ${price}", background="#faf9ed").place(x=260, y=500)
    Button(root, text="Edit items", command=edit_item_page_1).place(x=215, y=525)
    # Button(root, text="Checkout", command=checkout).place(x=305, y=525)


def edit_item_page_1():
    clear_window()
    back_button()
    global values, edit_item_spinbox
    values = []
    for i in supermarket_db.execute(f"SELECT ITEM FROM {table}"):
        values += i
    edit_item_label = Label(root, text="Item: ", background="#faf9ed")
    edit_item_spinbox = Spinbox(root, values=values, wrap=True)
    find_edit_item_button = Button(root, text="Continue", command=edit_item_check)
    delete_item_button = Button(root, text="Delete item", command=delete_item_check)
    edit_item_label.place(x=210, y=40)
    edit_item_spinbox.place(x=250, y=40)
    delete_item_button.place(x=220, y=80)
    find_edit_item_button.place(x=320, y=80)


def edit_item_check():
    if edit_item_spinbox.get() in values:
        global edit_item
        edit_item = edit_item_spinbox.get()
        edit_item_page_2()

    else:
        showerror("Edit Item Error", "Please enter an item in your basket")


def delete_item_check():
    if edit_item_spinbox.get() in values:
        global delete_item_val
        delete_item_val = edit_item_spinbox.get()
        delete_item()

    else:
        showerror("Delete Item Error", "Please enter an item that is in your basket")


def delete_item():
    supermarket_db.execute(f"DELETE FROM {table} WHERE ITEM = '{delete_item_val}'")
    ids = supermarket_db.execute(f"SELECT ID, ITEM FROM {table}")
    change_row = None
    id_list = []
    n = 1
    for i in ids:
        id_list.append(i[0])
    for k in id_list:
        if k > id_list.index(k):
            supermarket_db.execute(f"UPDATE {table} SET ID = {id_list.index(k) + 1} WHERE ID = {k}")
    print(change_row)
    supermarket_db.commit()
    show_basket()
    showinfo("Delete Item Success", "Successfully deleted item")


def edit_item_page_2():
    global edit_quantity_spinbox
    clear_window()
    back_button()
    editing_item_label = Label(root, text=f"Edit: {edit_item}", background="#faf9ed")
    edit_quantity_label = Label(root, text="Quantity: ", background="#faf9ed")
    edit_quantity_spinbox = Spinbox(root, from_=1, to=15, wrap=True)
    find_edit_item_button = Button(root, text="Edit Item", command=edit_item_do)
    editing_item_label.place(x=270, y=30)
    edit_quantity_label.place(x=200, y=70)
    edit_quantity_spinbox.place(x=260, y=70)
    find_edit_item_button.place(x=270, y=100)


def edit_item_do():
    supermarket_db.execute(f"UPDATE {table} SET QUANTITY = {edit_quantity_spinbox.get()}, "
                           f"PRICE = {float(get_price(edit_item)) * int(edit_quantity_spinbox.get())} "
                           f"WHERE ITEM = '{edit_item}'")

    supermarket_db.commit()
    show_basket()
    showinfo("Item successfully edited", "Item successfully edited")


def search_item():
    global search_photo, quantity_spinbox_search, search, search_upper
    search = search_entry.get().lower()
    if len(search) > 0:
        if search.lower() == "fruits":
            show_fruits()
            return None

        elif search.lower() == "vegetables":
            show_vegetables()
            return None

        elif search.lower() == "bakery":
            show_bakery()
            return None

        back_button()
        search_upper = f"{search[0].upper()}{search[1:].lower()}"
        homepage()

        try:
            search_photo = ImageTk.PhotoImage(
                Image.open(fr"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                           fr"Images\{search}.png"))

        except FileNotFoundError:
            showerror("Search error", "The searched product does not exist")
            return None
        image_label_search = Label(root, image=search_photo)
        item_label_search = Label(root, text=f"{search_upper}:   ${get_price(search_upper)}", background="#faf9ed")
        quantity_label_search = Label(root, text="Qty: ", background="#faf9ed")
        quantity_spinbox_search = Spinbox(root, from_=1, to=15, wrap=True, width=10)
        x, y = 200, 100
        image_label_search.place(x=x, y=y)
        item_label_search.place(x=x + 5, y=y + 80)
        quantity_label_search.place(x=x - 23, y=y + 100)
        quantity_spinbox_search.place(x=x + 5, y=y + 100)
        search_add_button = tk.Button(root, text="Add to basket", width=20, command=add_search_item)
        search_add_button.config(height=2, bg="#99ab93")
        search_add_button.place(x=400, y=500)

    else:
        showerror("Search Error", "Please enter a search")


def add_search_item():
    search_check = False
    search_results = []
    if quantity_spinbox_search.get() != "":
        if not quantity_spinbox_search.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from {table} where item = '{search_upper}')"):
                if i[0] == 1:
                    search_check = True

        if search_check:
            cursor = supermarket_db.execute(f"select price, quantity from {table} where item = '{search_upper}'")
            for i in cursor:
                search_results.append(i)

            supermarket_db.execute(f"update {table} set price = "
                                   f"{search_results[0][0] + (get_price(f'{search_upper}') * int(quantity_spinbox_search.get()))}, "
                                   f"quantity = {search_results[0][1] + int(quantity_spinbox_search.get())} "
                                   f"where item == '{search_upper}'")

        else:
            price = int(quantity_spinbox_search.get()) * get_price(f'{search_upper}')
            quantity = quantity_spinbox_search.get()
            supermarket_db.execute(f"INSERT INTO {table} (item, price, quantity)"
                                   f" VALUES ('{search_upper}', {price}, {quantity})")

        supermarket_db.commit()
        showinfo("Item(s) added", "The item(s) has/have successfully been added")


root = tk.Tk()
root.geometry("600x600")
root.title("Supermarket")
root.config(bg="#faf9ed")
supermarket_db = sql.connect(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\supermarket.db")
login_page()
root.mainloop()
