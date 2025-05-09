import Desktop.main_window
import CSVReader.csv_interpreter
import random

if __name__ == "__main__":
    all_games = CSVReader.csv_interpreter.csv_to_game_list()

    Desktop.main_window.create_and_start_main_window(all_games)