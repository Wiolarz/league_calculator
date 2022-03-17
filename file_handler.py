
def champions_stats_get_all():
    '''
    Returns a list of heroes basic statistics sheet as a dictionary.
    '''
    
    file = list(open("champions_stats.txt").read().split("\n"))
    
    stat_sheet = {
        "health": 0,
        "health_growth": 0,

        "hp_regen": 0,
        "hp_regen_growth": 0,

        "mana": 0,
        "mana_growth": 0,

        "mana_regen": 0,
        "mana_regen_growth": 0,

        "ad": 0,
        "ad_growth": 0,

        "as": 0,
        "as_growth": 0,

        "armor": 0,
        "armor_growth": 0,

        "magic_res": 0,
        "magic_res_growth": 0,

        "movement": 0,
        "range": 0,
        "bonus_as": 0}
    
    heroes = [] # {"name": "", "stats": {}}
    
    for line in file:  # Each hero has it's own line
        line = line.replace("+", "")
        line = line.replace("%", "")
        line = line.split("\t")
        # print(line)
        index = 0 # TODO check if this index is needed
        for stat in stat_sheet.keys():
            index += 1
            if index == 19:
                break
            try:
                stat_sheet[stat] = line[index]
            except:
                print(stat, index)
        heroes.append([line[0], stat_sheet])
    for hero in heroes:
        # print(hero)
        pass
    return heroes



class Stat:
    def __init__(self, type = None, stat = None):
        if stat == None:
            stat = 0
        if type == None:
            type = "health"

        self.stat = stat
        self.type = type

    def __repr__(self):
        return str(self.type) + " " + str(self.stat)


class Item:
    def __init__(self, cost = None, stats = None):
        if cost == None:
            cost = 0
        if stats == None:
            stats = []
        self.stats = stats
        self.cost = cost

    '''    def __str__(self):
        #text = self.cost, self.stats
        return self.cost'''

    def __repr__(self):
        return str(self.cost) + "g " + str(self.stats)


def starter_items_get_all():
    '''
    Returns: list of arrays [item_name, Item object]
    '''
    
    file = list(open("starter_items_stats.txt").read().split("\n"))
    
    items = []  # {"name": "", "item_object": {}}
    
    for line in file:
        line = line.split("\t")
        # print(line)
        
        stats = []
        for index in range(3, len(line), 2):
            # loop provides pairs of indexes that provide a name of a statistic and it's value
            stats.append(Stat(line[index - 1], line[index]))

        new_item = Item(line[1], stats)
        items.append([line[0], new_item])

    for item in items:
        # print(item)
        pass
    return items
