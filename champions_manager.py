import file_handler
import game_logic


"""
File for managing data from file handler and strategy builder
"""





def champions_create_objects(file=None):
    """
    Converts champions statistics sheets into champions level 1 objects
    :param file: champions statistics sheets
    :return: list of champions level 1 objects
    """
    if file == None:
        file = file_handler.champions_stats_get_all()

    champions_database = []
    for character in file:
        champions_database.append(game_logic.Player(game_logic.Champion(character[0], character[1])))
    return champions_database


def champions_database_levelup(database, desired_level):
    pass#for champion in database:
