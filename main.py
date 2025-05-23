import Desktop.main_window
import CSVReader.csv_interpreter
import random

if __name__ == "__main__":
    all_games = CSVReader.csv_interpreter.csv_to_game_list()

    filtered_games = []

    for game in all_games:
        if game.status == "Completed" or game.status == "Beaten" or game.status == "None" or game.ownership == "Wishlist":
            continue

        filtered_games.append(game)

    Desktop.main_window.create_and_start_main_window(filtered_games)