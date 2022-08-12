from tkinter import *
from tkinter.ttk import *

root = Tk()
button = Button(root, text="Try to get this")
button.pack()
print(button['text'])
mainloop()
