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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("start")
    #game_logic.test()
    #file_handler.champions_stats_get_all()
    starter_item_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
