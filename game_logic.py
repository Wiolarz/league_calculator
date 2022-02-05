'''

First version aims to calculate HP value of a champion based on his level
Code structure:
Each time we try new item combination we test it on a player which consists of a
hero object - base statistics and skills
    can be modified by level and sometimes which skills he had already leveled up in order to test early game
Backpack object - 6 items slots + potion effect
Runes page
dragon/baron/golem/other heroes buffs

'''

class Champion:
    def __init__(self, stats):
        self.base_data = {"health": stats["health"], "hp_regen": stats["hp_regen"], "armor": stats["armor"],
                          "magic_res": stats["magic_res"], "mana": stats["mana"], "mana_regen": stats["mana_regen"],
                          "ad": stats["ad"], "aa_speed": 0, "ap": 0, "armor_pen": 0, "critical_chance": 0,
                          "critical_dmg": 0, "lifesteal": 0, "magic_pen": 0, "omnivamp": 0, "physival_vamp": 0,
                          "heal_shield": 0, "tenacity": 0, "slow_res": 0, "ability_haste": 0, "as": stats["as"]}

        self.data = self.base_data.copy()


    def aa_dps(self):
        return self.ad * self.aa_speed

    def apply_items(self, bag):
        self.data = self.base_data.copy()  # before applying new items statistics we rest champion values
        for item in bag:
            if item != None:
                for attribute in item.stats:
                    self.data[attribute.type] += attribute.stat





class Player:
    def __init__(self, champion, bag = None):
        if bag == None:
            bag = []
        self.champion = champion  # object champion
        self.bag = bag  # is an array of the maximum size of 6 of objects "items"

    def equip_items(self):
        self.champion.apply_items(self.bag)



def champion_levelup(level, base_sheet):
    # this method takes a champion stat sheet and the desired level and returns updated values
    """ growth of statistics
     Statistic = b + (g * (n - 1) * (0.7025 + (0.0175 * (n - 1))))  # general equation
     statIncrease = g * (0.65 + (0.035 * new_level)  # used in the code
     b = base, g = growth statistic, n champion level
     """

    stats = base_sheet.copy()

    for i_level in range(2, level + 1):
        multiplier = 0.65 + (0.035 * i_level)
        stats["health"]     += stats["health_growth"]     * multiplier
        stats["hp_regen"]   += stats["hp_regen_growth"]   * multiplier
        stats["armor"]      += stats["armor_growth"]      * multiplier
        stats["magic_res"]  += stats["magic_res_growth"]  * multiplier
        stats["mana"]       += stats["mana_growth"]       * multiplier
        stats["mana_regen"] += stats["mana_regen_growth"] * multiplier
        stats["ad"]         += stats["ad_growth"]         * multiplier
        stats["bonus_as"]   += stats["as_growth"]         * multiplier
    return stats




def ashe_tester():
    stat_sheet ={# example Ashe statistics
                "health": 570,
                "hp_regen": 3.5,
                "armor": 26,
                "magic_res": 30,
                "mana": 280,
                "mana_regen": 6.97,
                "ad": 59,
                "as": 0.658,
                "bonus_as": 0,

                "health_growth": 87,
                "hp_regen_growth": 0.55,
                "armor_growth": 3.4,
                "magic_res_growth": 0.5,
                "mana_growth": 32,
                "mana_regen_growth": 0.4,
                "ad_growth": 2.96,
                "as_growth": 3.33,

                "movement": 325,
                "range": 600}

    champion = Champion(stat_sheet)


    #shield = Item()

    #bag.items.append(shield)

    #player = Player(champion, bag)


    #ashe = champion_levelup(10, stat_sheet)

    return champion


