from Game import *

def csv_to_game_list() -> list[Game]:
    text = open("CSVFiles/mainLibrary.csv", "r")
    text = ' '.join([i for i in text])

    text = trim_top_text(text, 3)

    game_entries = text.split('"\n')

    game_list_array = []

    for game_entry in game_entries:
        game_entry_properties = game_entry.split(',')

        if len(game_entry_properties) < 3:
            continue

        game = create_game_object(game_entry_properties)
        game_list_array.append(game)

    return game_list_array


def trim_top_text(text: str, parts: int) -> str:
    text_parts = text.split('\n', parts)
    if len(text_parts) > parts:
        return text_parts[parts]
    else:
        return ''


def create_game_object(properties: list[str]) -> Game:
    id = int(properties[0].replace(" ", ""))

    title = properties[1]

    platform = properties[2]

    sub_platform = properties[3]

    status = properties[4]

    priority = properties[5]

    format = properties[6]

    ownership = properties[7]

    notes = properties[8]  #Replace later with all notes

    if properties[-2] is not "":
        child_of = int(properties[-2].replace(" ", ""))
    else:
        child_of = None

    last_updated = properties[-1]

    return_game = Game(id, title, platform, sub_platform, status, priority, format, ownership, notes, child_of,
                       last_updated)

    return return_game
