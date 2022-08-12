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
    global apple_photo, banana_photo, quantity_entry_apple, quantity_entry_banana
    apple_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                r"Images\apple.png"))
    image_label_apple = Label(root, image=apple_photo)
    item_label_apple = Label(root, text=f"Apple:   ${get_price('Apple')}", background="#faf9ed")
    quantity_label_apple = Label(root, text="Qty: ", background="#faf9ed")
    quantity_entry_apple = Entry(root, width=10)
    x, y = 200, 100
    image_label_apple.place(x=x, y=y)
    item_label_apple.place(x=x + 5, y=y + 80)
    quantity_label_apple.place(x=x - 23, y=y + 100)
    quantity_entry_apple.place(x=x + 5, y=y + 100)

    banana_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\banana.png"))
    image_label_banana = Label(root, image=banana_photo)
    item_label_banana = Label(root, text=f"Banana:   ${get_price('Banana')}", background="#faf9ed")
    quantity_label_banana = Label(root, text="Qty: ", background="#faf9ed")
    quantity_entry_banana = Entry(root, width=10)
    x = 370
    image_label_banana.place(x=x, y=y)
    item_label_banana.place(x=x, y=y + 80)
    quantity_label_banana.place(x=x - 23, y=y + 100)
    quantity_entry_banana.place(x=x + 5, y=y + 100)
    add_button = tk.Button(root, text="Add to basket", width=20, command=add_items_fruits)
    add_button.config(height=2, bg="#99ab93")
    add_button.place(x=400, y=500)


def show_vegetables():
    clear_window()
    homepage()
    back_button()
    global carrot_photo, potato_photo, quantity_entry_carrot, quantity_entry_potato
    carrot_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\carrot.png"))
    image_label_carrot = Label(root, image=carrot_photo)
    item_label_carrot = Label(root, text=f"Carrot:   ${get_price('Carrot')}", background="#faf9ed")
    quantity_label_carrot = Label(root, text="Qty: ", background="#faf9ed")
    quantity_entry_carrot = Entry(root, width=10)
    x, y = 200, 100
    image_label_carrot.place(x=x, y=y)
    item_label_carrot.place(x=x + 5, y=y + 80)
    quantity_label_carrot.place(x=x - 23, y=y + 100)
    quantity_entry_carrot.place(x=x + 5, y=y + 100)

    potato_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                 r"Images\potato.png"))
    image_label_potato = Label(root, image=potato_photo)
    item_label_potato = Label(root, text=f"Potato:   ${get_price('Potato')}", background="#faf9ed")
    quantity_label_potato = Label(root, text="Qty: ", background="#faf9ed")
    quantity_entry_potato = Entry(root, width=10)
    x = 370
    image_label_potato.place(x=x, y=y)
    item_label_potato.place(x=x, y=y + 80)
    quantity_label_potato.place(x=x - 23, y=y + 100)
    quantity_entry_potato.place(x=x + 5, y=y + 100)
    add_button = tk.Button(root, text="Add to basket", width=20, command=add_items_vegetables)
    add_button.config(height=2, bg="#99ab93")
    add_button.place(x=400, y=500)


def show_bakery():
    clear_window()
    homepage()
    back_button()
    global bread_photo, cake_photo, quantity_entry_bread, quantity_entry_cake
    bread_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                                r"Images\bread.png"))
    image_label_bread = Label(root, image=bread_photo)
    item_label_bread = Label(root, text=f"Bread:   ${get_price('Bread')}", background="#faf9ed")
    quantity_label_bread = Label(root, text="Qty: ", background="#faf9ed")
    quantity_entry_bread = Entry(root, width=10)
    x, y = 200, 100
    image_label_bread.place(x=x, y=y)
    item_label_bread.place(x=x + 5, y=y + 80)
    quantity_label_bread.place(x=x - 23, y=y + 100)
    quantity_entry_bread.place(x=x + 5, y=y + 100)

    cake_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\adi09\PycharmProjects\TKinter\Supermarket\Supermarket"
                                               r"Images\cake.png"))
    image_label_cake = Label(root, image=cake_photo)
    item_label_cake = Label(root, text=f"Cake:   ${get_price('Cake')}", background="#faf9ed")
    quantity_label_cake = Label(root, text="Qty: ", background="#faf9ed")
    quantity_entry_cake = Entry(root, width=10)
    x = 370
    image_label_cake.place(x=x, y=y)
    item_label_cake.place(x=x, y=y + 80)
    quantity_label_cake.place(x=x - 23, y=y + 100)
    quantity_entry_cake.place(x=x + 5, y=y + 100)
    add_button = tk.Button(root, text="Add to basket", width=20, command=add_items_bakery)
    add_button.config(height=2, bg="#99ab93")
    add_button.place(x=400, y=500)


def add_items_fruits():
    apple_check = False
    apple_results = []
    if quantity_entry_apple.get() != "":
        if not quantity_entry_apple.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute("select exists (select 1 from basket where item = 'Apple')"):
                if i[0] == 1:
                    apple_check = True

        if apple_check:
            cursor = supermarket_db.execute("select price, quantity from basket where item = 'Apple'")
            for i in cursor:
                apple_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{apple_results[0][0] + (get_price('Apple') * int(quantity_entry_apple.get()))}, "
                                   f"quantity = {apple_results[0][1] + int(quantity_entry_apple.get())} "
                                   f"where item == 'Apple'")

        else:
            price = int(quantity_entry_apple.get()) * get_price('Apple')
            quantity = quantity_entry_apple.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('Apple', {price}, {quantity})")

    banana_check = False
    banana_results = []
    if quantity_entry_banana.get() != "":
        if not quantity_entry_banana.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute("select exists (select 1 from basket where item = 'Banana')"):
                if i[0] == 1:
                    banana_check = True

        if banana_check:
            cursor = supermarket_db.execute("select price, quantity from basket where item = 'Banana'")
            for i in cursor:
                banana_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{banana_results[0][0] + (get_price('Banana') * int(quantity_entry_banana.get()))},"
                                   f" quantity = {banana_results[0][1] + int(quantity_entry_banana.get())} "
                                   f"where item == 'Banana'")

        else:
            price = int(quantity_entry_banana.get()) * get_price('Banana')
            quantity = quantity_entry_banana.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('Banana', {price}, {quantity})")

    supermarket_db.commit()
    showinfo("Item(s) added", "The item(s) has/have successfully been added")
    show_fruits()


def add_items_vegetables():
    carrot_check = False
    carrot_results = []
    if quantity_entry_carrot.get() != "":
        if not quantity_entry_carrot.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute("select exists (select 1 from basket where item = 'Carrot')"):
                if i[0] == 1:
                    carrot_check = True

        if carrot_check:
            cursor = supermarket_db.execute("select price, quantity from basket where item = 'Carrot'")
            for i in cursor:
                carrot_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{carrot_results[0][0] + (get_price('Carrot') * int(quantity_entry_carrot.get()))},"
                                   f" quantity = {carrot_results[0][1] + int(quantity_entry_carrot.get())} "
                                   f"where item == 'Carrot'")

        else:
            price = int(quantity_entry_carrot.get()) * get_price('Carrot')
            quantity = quantity_entry_carrot.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('Carrot', {price}, {quantity})")

    potato_check = False
    potato_results = []
    if quantity_entry_potato.get() != "":
        if not quantity_entry_potato.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute("select exists (select 1 from basket where item = 'Potato')"):
                if i[0] == 1:
                    potato_check = True

        if potato_check:
            cursor = supermarket_db.execute("select price, quantity from basket where item = 'Potato'")
            for i in cursor:
                potato_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{potato_results[0][0] + (get_price('Potato') * int(quantity_entry_potato.get()))},"
                                   f" quantity = {potato_results[0][1] + int(quantity_entry_potato.get())} "
                                   f"where item == 'Potato'")

        else:
            price = int(quantity_entry_potato.get()) * get_price('Potato')
            quantity = quantity_entry_potato.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('Potato', {price}, {quantity})")

    supermarket_db.commit()
    showinfo("Item(s) added", "The item(s) has/have successfully been added")
    show_vegetables()


def add_items_bakery():
    bread_check = False
    bread_results = []
    if quantity_entry_bread.get() != "":
        if not quantity_entry_bread.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute("select exists (select 1 from basket where item = 'Bread')"):
                if i[0] == 1:
                    bread_check = True

        if bread_check:
            cursor = supermarket_db.execute("select price, quantity from basket where item = 'Bread'")
            for i in cursor:
                bread_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{bread_results[0][0] + (get_price('Bread') * int(quantity_entry_bread.get()))}, "
                                   f"quantity = {bread_results[0][1] + int(quantity_entry_bread.get())} "
                                   f"where item == 'Bread'")

        else:
            price = int(quantity_entry_bread.get()) * get_price('Bread')
            quantity = quantity_entry_bread.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('Bread', {price}, {quantity})")

    cake_check = False
    cake_results = []
    if quantity_entry_cake.get() != "":
        if not quantity_entry_cake.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute("select exists (select 1 from basket where item = 'Cake')"):
                if i[0] == 1:
                    cake_check = True

        if cake_check:
            cursor = supermarket_db.execute("select price, quantity from basket where item = 'Cake'")
            for i in cursor:
                cake_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{cake_results[0][0] + (get_price('Cake') * int(quantity_entry_cake.get()))}, "
                                   f"quantity = {cake_results[0][1] + int(quantity_entry_cake.get())} "
                                   f"where item == 'Cake'")

        else:
            price = int(quantity_entry_cake.get()) * get_price('Cake')
            quantity = quantity_entry_cake.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('Cake', {price}, {quantity})")

    supermarket_db.commit()
    showinfo("Item(s) added", "The item(s) has/have successfully been added")
    show_bakery()


def show_basket():
    clear_window()
    back_button()
    cursor = supermarket_db.execute("SELECT * FROM BASKET")
    x, y = 250, 100
    price = 0.0
    global small_img
    for i in cursor:
        price += round(i[2], 2)
        small_img = ImageTk.PhotoImage(Image.open(fr"SupermarketImages\small_{i[1].lower()}.png"))
        img_label = Label(root, image=small_img)
        item_label = Label(root, text=f"{i[1]} x {i[3]}        ${round(i[2], 2)}", background="#faf9ed")
        img_label.place(x=x, y=y)
        item_label.place(x=x + 40, y=y + 10)
        y += 40
    Label(root, text=f"Total:     ${price}", background="#faf9ed").place(x=260, y=500)


def search_item():
    global search_photo, quantity_entry_search, search, search_upper
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
        quantity_entry_search = Entry(root, width=10)
        x, y = 200, 100
        image_label_search.place(x=x, y=y)
        item_label_search.place(x=x + 5, y=y + 80)
        quantity_label_search.place(x=x - 23, y=y + 100)
        quantity_entry_search.place(x=x + 5, y=y + 100)
        search_add_button = tk.Button(root, text="Add to basket", width=20, command=add_search_item)
        search_add_button.config(height=2, bg="#99ab93")
        search_add_button.place(x=400, y=500)

    else:
        showerror("Search Error", "Please enter a search")


def add_search_item():
    search_check = False
    search_results = []
    if quantity_entry_search.get() != "":
        if not quantity_entry_search.get().isnumeric():
            showerror("Invalid Input", "Please ensure your quantities are numbers")

        else:
            for i in supermarket_db.execute(f"select exists (select 1 from basket where item = '{search_upper}')"):
                if i[0] == 1:
                    search_check = True

        if search_check:
            cursor = supermarket_db.execute(f"select price, quantity from basket where item = '{search_upper}'")
            for i in cursor:
                search_results.append(i)

            supermarket_db.execute(f"update basket set price = "
                                   f"{search_results[0][0] + (get_price(f'{search_upper}') * int(quantity_entry_search.get()))}, "
                                   f"quantity = {search_results[0][1] + int(quantity_entry_search.get())} "
                                   f"where item == '{search_upper}'")

        else:
            price = int(quantity_entry_search.get()) * get_price(f'{search_upper}')
            quantity = quantity_entry_search.get()
            supermarket_db.execute(f"INSERT INTO basket (item, price, quantity)"
                                   f" VALUES ('{search_upper}', {price}, {quantity})")

        supermarket_db.commit()
        showinfo("Item(s) added", "The item(s) has/have successfully been added")


root = tk.Tk()
root.geometry("600x600")
root.title("Supermarket")
root.config(bg="#faf9ed")
supermarket_db = sql.connect("supermarket.db")
supermarket_db.execute("DELETE FROM BASKET")
supermarket_db.execute("UPDATE `sqlite_sequence` SET `seq` = 1 WHERE `name` = 'basket'")
supermarket_db.commit()
homepage()
root.mainloop()
supermarket_db.close()
