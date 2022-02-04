#include <iostream>
#include <map>
#include <fstream>





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









class Backpack:
    def __init__(self, items = None):
        if items == None:
            items = []
        self.items = items


class Champion:

    def __init__(self, stats):

        self.health = stats["health"]
        self.hp_regen = stats["hp_regen"]
        self.armor = stats["armor"]
        self.magic_res = stats["magic_res"]
        self.mana = stats["mana"]
        self.mana_regen = stats["mana_regen"]
        self.ad = stats["ad"]
        self.aa_speed = stats["as"]  # auto attack speed

        self.ap = 0

        self.ap = 0
        self.armor_pen = 0
        self.critical_chance = 0
        self.critical_dmg = 0
        self.lifesteal = 0
        self.magic_pen = 0
        self.omnivamp = 0
        self.physival_vamp = 0
        self.heal_shield = 0
        self.tenacity = 0
        self.slow_res = 0
        self.ability_haste = 0

    def aa_dps(self):
        return self.ad * self.aa_speed



class Player:
    def __init__(self, champion, bag):
        self.champion = champion
        self.bag = bag



def champion_levelup(level, base_sheet):
    # this method takes a champion stat sheet and the desired level and returns updated values

    ''' growth of statistics
     Statistic = b + (g * (n - 1) * (0.7025 + (0.0175 * (n - 1))))
     b = base, g = growth statistic, n champion level
     g'''


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




def test():

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
    bag = Backpack()

    #shield = Item()

    #bag.items.append(shield)

    #player = Player(champion, bag)

    print(stat_sheet["health"])
    ashe = champion_levelup(10, stat_sheet)

    print(ashe["health"])


