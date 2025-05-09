import tkinter as tk
from tkinter import ttk
import Game

def create_and_start_main_window(game_data: list[Game]):
    window = tk.Tk()
    window.title("Backloggery Priority Manager")

    columns = ("unique_game_id", "title", "platform", "sub_platform", "status", "priority", "format", "ownership", "notes", "child_of", "last_updated")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

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

    window.mainloop()
