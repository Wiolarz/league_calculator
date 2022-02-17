import game_logic
import items_manager
import champions_manager
import combat



def champion_hp_max(player, items):
    """
    Calculate champion maximum possible Health value
    :param player:
    :param items: database of items
    :return: champions maximum health value
    """
    max_hp = float(player.champion.data["health"])
    #print(max_hp)
    for bag in items:
        player.bag = bag
        player.equip_items()
        if max_hp < player.champion.data["health"]:
            max_hp = player.champion.data["health"]
    return max_hp

def champions_hp_max_testing_enviro(champions_database, items_database):
    """
    Find champion with maximum possible Health value and get that value
    :param champions_database:
    :param items_database:
    :return:
    """
    max_hp = champions_database[0].champion.data["health"]
    max_name = champions_database[0].champion.name
    for champion in champions_database:                         # for each champion
        result = champion_hp_max(champion, items_database)
        if max_hp < result:
            max_hp = result
            max_name = champion.champion.name
        print(champion.champion.name, result)
    print(max_name, max_hp)
    return max_name, max_hp


def champions_max_hp_testing():
    items_database = items_manager.starter_item_test()
    # items_database = [[file_handler.Item("shield", 10, [file_handler.Stat("health", 100)])]]
    champions_database = champions_manager.champions_create_objects()
    champions_hp_max_testing_enviro(champions_database, items_database)


if __name__ == '__main__':
    print("start of the main file")
    #game_logic.test()
    #file_handler.champions_stats_get_all()

    champions_database = champions_manager.champions_create_objects()

    combat.champion_durability(champions_database[0].champion, champions_database[1].champion)



