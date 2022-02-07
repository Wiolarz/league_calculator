"""
File for managing items and creating builds
"""
import file_handler

def starter_item_test():
    items = file_handler.starter_items_get_all()
    #print(items)
    result = test_basic_items_permutation(items)
    #for bag in result:
        #print(bag)
    print(len(result))
    return result

def include_only_durability_items(items_database):
    """

    :param items_database:
    :return:
    """
    reduced_list = []
    durability_stat_list = ["health", "hp_regen", "armor", "magic_res"]
    for item in items_database:
        for stat in item.stats:
            if stat in durability_stat_list:
                reduced_list.append(item)
                break
    return reduced_list


def test_basic_items_permutation(basic_items_list):
    """
    :param basic_items_list:
    :return:
    """
    basic_items_list.append(None)
    result = []
    for item_1 in basic_items_list:
        for item_2 in basic_items_list:
            for item_3 in basic_items_list:
                for item_4 in basic_items_list:
                    for item_5 in basic_items_list:
                        for item_6 in basic_items_list:
                            bag = []
                            items = [item_1, item_2, item_3, item_4, item_5, item_6]
                            for item in items:
                                if item != None:
                                    bag.append(item)
                            result.append(bag)
    return result

def test2(items_list):
    used = -1
    for item1 in items_list:
        pass






def test_basic_items(player, basic_items_list):
    """
    This method is a demo of desired function.
    List of simplifications present in this demo:
    use of only basic items list, no items repetition
    :param player:
    :param basic_items_list: already prepared long list of every possible combination
    :return:
    """