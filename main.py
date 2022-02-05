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


def champion_hp_max(items):
    ashe = game_logic.ashe_tester()
    player = game_logic.Player(ashe)
    max_hp = float(player.champion.data["health"])
    print(max_hp)
    for bag in items:
        ashe.apply_items(bag)
        if max_hp < player.champion.data["health"]:
            max_hp = player.champion.data["health"]
    print(max_hp)

if __name__ == '__main__':
    print("start")
    #game_logic.test()
    #file_handler.champions_stats_get_all()

    items_database = starter_item_test()
    #items_database = [[file_handler.Item("shield", 10, [file_handler.Stat("health", 100)])]]
    champion_hp_max(items_database)


