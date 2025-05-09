import Desktop.main_window
import CSVReader.csv_interpreter
import random

if __name__ == "__main__":
    # Test Code delete later
    all_games = CSVReader.csv_interpreter.csv_to_game_list()
    print(all_games[random.randint(0, len(all_games))])

    Desktop.main_window.CreateAndStartMainWindow()