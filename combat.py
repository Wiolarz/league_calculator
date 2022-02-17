"""
File for simulating combat in order to test champions builds
"""





def champion_durability(attacker, defender):
    """
    Basic tests for auto attack damage
    :param attacker:
    :param defender:
    :return:
    """



    time_between_attacks = attacker.auto_attack_speed()
    if time_between_attacks <= 0:
        print("error")
        return

    regen_time = 0
    for attack_counter in range(1000):
        defender.receive_damage(attacker.auto_attack(), "ad")

        if defender.hp <= 0:
            print(attack_counter)
            return
        regen_time += time_between_attacks

        # every half a second defender regenerates his HP
        while regen_time >= 0.5:
            defender.regenerate_health()
            regen_time -= 0.5
    print("cannot die")

