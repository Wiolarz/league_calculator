"""
Functions in this files will take players and items lists, then mix those items into every possible build
finally printing results
"""

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




def test_basic_items(player, basic_items_list):
    """
    This method is a demo of desired function.
    List of simplifications present in this demo:
    use of only basic items list, no items repetition
    :param player:
    :param basic_items_list: already prepared long list of every possible combination
    :return:
    """
