"""
File for simulating combat in order to test champions builds
"""





def champion_durability(attacker, defender):
    """
    Basic tests for auto attack damage
    :param attacker: Player
    :param defender: Player
    :return:
    """



    time_between_attacks = attacker.champion.auto_attack_speed()
    if time_between_attacks <= 0:
        print("error")
        return -2

    regen_time = 0
    for attack_counter in range(1000):
        defender.champion.receive_damage(attacker.champion.auto_attack(), "ad")

        if defender.champion.hp <= 0:
            # print(attack_counter)
            return attack_counter
        regen_time += time_between_attacks

        # every half a second defender regenerates his HP
        while regen_time >= 0.5:
            defender.champion.regenerate_health()
            regen_time -= 0.5
    print("cannot die")
    return -1

