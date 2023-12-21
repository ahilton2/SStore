
Merchandise = {"Short Sleeve Black Bleached Penguin Shirt": 10, "Short Sleeve Red Shirt": 10, "Subpenguin Bracelet": 3}
Shows = {"White Swan":"Saturday, December 16", "Ojeman":"ur mom O clock"}
User_Name = input("What should we refer to you as?")
User_Name = User_Name.lower()
User_Name = User_Name.capitalize()
print("Hello, " + User_Name + ", what can I help you with today?")

import tkinter as tk
from tkinter import ttk

def on_option_selected(event):
    selected_option = combo.get()
    print("You selected:", selected_option)

root = tk.Tk()
root.title("Dropdown-like Menu")
Problem_Choices = ["I'd like to buy merch", "I'd like a list of your upcoming shows", "I'm Sad :'(" ]
combo = ttk.Combobox(root, values=Problem_Choices)
combo.set("Select an option")
combo.bind("<<ComboboxSelected>>", on_option_selected)
combo.pack(pady=10)
root.mainloop()
