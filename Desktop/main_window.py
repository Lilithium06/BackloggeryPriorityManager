import tkinter as tk
from tkinter import ttk, Label
import Game
import random

def create_and_start_main_window(game_data: list[Game]):
    window = tk.Tk()
    window.title("Backloggery Priority Manager")
    window.state("zoomed")

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)

    columns = ("title", "platform", "sub_platform", "status", "priority", "elo")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)
    tree.grid(row = 0, column = 0, sticky="nsew")

    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())

    for game in game_data:
        values = (
            str(game.title).replace('"', "'"),
            str(game.platform).replace('"', "'"),
            str(game.sub_platform).replace('"', "'"),
            str(game.status).replace('"', "'"),
            str(game.priority).replace('"', "'"),
            str(game.elo).replace('"', "'")
        )

        # Use status as a tag
        tree.insert("", "end", values=values, iid=game.unique_game_id)

    # Frame to hold pairwise comparison
    pair_frame = ttk.Frame(window)
    pair_frame.grid(row=0, column=2, padx=20, pady=20, sticky="n")

    # Labels for the two games
    game1_label = ttk.Label(pair_frame, text="", width=50, wraplength=200, justify="center")
    game1_label.grid(row=0, column=0, padx=10)

    game2_label = ttk.Label(pair_frame, text="", width=50, wraplength=200, justify="center")
    game2_label.grid(row=0, column=2, padx=10)

    def get_random_pair(data):
        return random.sample(data, 2)

    def choose_game(won_game, lost_game, k=32):
        expected_won_game = 1 / (1 + 10 ** ((lost_game.elo - won_game.elo) / 400))
        won_game.elo += k * (1 - expected_won_game)
        lost_game.elo -= k * expected_won_game

        won_game_values = list(tree.item(won_game.unique_game_id, "values"))
        won_game_values[5] = won_game.elo
        tree.item(won_game.unique_game_id, values=won_game_values)

        lost_game_values = list(tree.item(lost_game.unique_game_id, "values"))
        lost_game_values[5] = lost_game.elo
        tree.item(lost_game.unique_game_id, values=lost_game_values)

        sort_tree()

        show_new_pair()

    def show_new_pair():
        g1, g2 = get_random_pair(game_data)
        game1_label.config(text=f"{g1.title}\n({g1.platform})")
        game2_label.config(text=f"{g2.title}\n({g2.platform})")

        button1.config(command=lambda: choose_game(g1, g2))
        button2.config(command=lambda: choose_game(g2, g1))

    def sort_tree():
        items = tree.get_children()

        data = []
        for item in items:
            item_values = tree.item(item, "values")
            elo = float(item_values[5])
            title = item_values[0]
            data.append((elo, title, item, item_values))

        data.sort(key=lambda x: (-x[0], x[1]))

        for item in items:
            tree.delete(item)

        for _,_, iid, item_values in data:
            tree.insert("", "end", iid=iid, values=item_values)


    button1 = ttk.Button(pair_frame, text="Pick Left")
    button1.grid(row=1, column=0, pady=10)

    button2 = ttk.Button(pair_frame, text="Pick Right")
    button2.grid(row=1, column=2, pady=10)

    show_new_pair()

    window.mainloop()

