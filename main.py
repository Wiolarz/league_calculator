import file_handler
import game_logic
import strategy_builder

def starter_item_test():
    items = file_handler.starter_items_get_all()
    #print(items)
    result = strategy_builder.test_basic_items_permutation(items)
    #for bag in result:
        #print(bag)
    print(len(result))
    return result


def champion_hp_max(player, items):
    max_hp = float(player.champion.data["health"])
    #print(max_hp)
    for bag in items:
        player.bag = bag
        player.equip_items()
        if max_hp < player.champion.data["health"]:
            max_hp = player.champion.data["health"]
    return max_hp

def champions_hp_max_testing_enviro(champions_database, items_database):
    max_hp = champions_database[0].champion.data["health"]
    max_name = champions_database[0].champion.name
    for champion in champions_database:
        result = champion_hp_max(champion, items_database)
        if max_hp < result:
            max_hp = result
            max_name = champion.champion.name
        print(champion.champion.name, result)
    print(max_name, max_hp)

def champions_create_objects(file):
    champions_database = []
    for character in file:
        champions_database.append(game_logic.Player(game_logic.Champion(character[0], character[1])))
    return champions_database

if __name__ == '__main__':
    print("start")
    #game_logic.test()
    #file_handler.champions_stats_get_all()

    items_database = starter_item_test()
    #items_database = [[file_handler.Item("shield", 10, [file_handler.Stat("health", 100)])]]
    file = file_handler.champions_stats_get_all()
    champions_database = champions_create_objects(file)
    champions_hp_max_testing_enviro(champions_database, items_database)


