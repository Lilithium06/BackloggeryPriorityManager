import tkinter as tk
from tkinter import ttk, Label
import Game

def create_and_start_main_window(game_data: list[Game]):
    window = tk.Tk()
    window.title("Backloggery Priority Manager")
    window.state("zoomed")

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)

    columns = ("title", "platform", "sub_platform", "status", "priority", "format", "ownership")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)
    tree.grid(row = 0, column = 0, sticky="nsew")

    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())

    # Define tag styles for statuses based on the image
    tree.tag_configure("Unplayed", background="#2d3f4e")    # dark blue-gray
    tree.tag_configure("Unfinished", background="#8a4c48")  # muted red-brown
    tree.tag_configure("Beaten", background="#bdbdbd")      # light gray
    tree.tag_configure("Completed", background="#e1d08f")   # pale yellow

    for game in game_data:
        if game.ownership == "Wishlist":
            continue

        status = str(game.status).replace('"', "'")
        values = (
            str(game.title).replace('"', "'"),
            str(game.platform).replace('"', "'"),
            str(game.sub_platform).replace('"', "'"),
            status,
            str(game.priority).replace('"', "'"),
            str(game.format).replace('"', "'"),
            str(game.ownership).replace('"', "'")
        )

        # Use status as a tag
        tree.insert("", "end", values=values, tags=(status if status in ["Unplayed", "Unfinished", "Beaten", "Completed"] else ""))

    label1 = Label(window, text ="This is a test")
    label1.grid(row = 0, column = 2)

    window.mainloop()