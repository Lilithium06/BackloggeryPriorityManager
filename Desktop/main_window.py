import tkinter as tk
from tkinter import ttk, Label
import tkinter.font as tkFont
import Game

def create_and_start_main_window(game_data: list[Game]):
    window = tk.Tk()
    window.title("Backloggery Priority Manager")
    window.state("zoomed")

    columns = ("unique_game_id", "title", "platform", "sub_platform", "status", "priority", "format", "ownership", "notes", "child_of", "last_updated")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.column("unique_game_id", width = 100)
    tree.column("format", width = 70)
    tree.column("ownership", width = 150)
    tree.column("last_updated", width = 100)
    tree.pack(fill="both", expand=True)
    tree.grid(row = 0, column = 0, columnspan = 2)

    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())

    # Define tag styles for statuses based on the image
    tree.tag_configure("Unplayed", background="#2d3f4e")    # dark blue-gray
    tree.tag_configure("Unfinished", background="#8a4c48")  # muted red-brown
    tree.tag_configure("Beaten", background="#bdbdbd")      # light gray
    tree.tag_configure("Completed", background="#e1d08f")   # pale yellow

    for game in game_data:
        status = str(game.status).replace('"', "'")
        values = (
            str(game.unique_game_id),
            str(game.title).replace('"', "'"),
            str(game.platform).replace('"', "'"),
            str(game.sub_platform).replace('"', "'"),
            status,
            str(game.priority).replace('"', "'"),
            str(game.format).replace('"', "'"),
            str(game.ownership).replace('"', "'"),
            str(game.notes).replace('"', "'") if game.notes else "",
            str(game.child_of) if game.child_of else "",
            str(game.last_updated)
        )

        # Use status as a tag
        tree.insert("", "end", values=values, tags=(status if status in ["Unplayed", "Unfinished", "Beaten", "Completed"] else ""))

    auto_resize_columns(tree)

    label1 = Label(window, text = "This is a test")
    label1.grid(row = 0, column = 2)

    window.mainloop()

def auto_resize_columns(treeview):
    font = tkFont.Font()
    for col in treeview["columns"]:
        max_width = font.measure(col)  # Start with header width
        for item in treeview.get_children():
            cell_value = treeview.set(item, col)
            width = font.measure(str(cell_value))
            if width > max_width:
                max_width = width
        treeview.column(col, width=max_width + 10)  # Add padding
    treeview.column("notes", width=100)
