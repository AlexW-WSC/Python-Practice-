import random
player_name = input("Please enter your name to begin.").strip()
if len((player_name)) >= 15:
    player_name = input("Please enter your name to begin.").strip()

global player_max_hp 
player_max_hp = 100
global player_hp 
player_hp = 100

global player_max_mana
player_max_mana = 100
global player_mana 
player_mana = 100

decision = 0


game_map = {
    (-1, 1): "Shop",
    (0, 1): "Home",
    (1, 1): "Forest",
    (-1, 0): "Cave",
    (0, 0): "Spawn",  
    (1, 0): "River",
    (0, -1): "MysticDragonCave"  
}

player_position = (0,0)


def draw_map(centre):
    x0, y0 = centre
    print(centre)
    for y in range(y0 + 1, y0 - 1):
        row = []
        for x in range(x0 - 1, x0 +1):
            if (x, y) == player_position:
                tile = "[You!]"
            else:
                tile = game_map.get((x,y), "     ")







# -------- code for the combat system


# player equipment indexes!!

weapon_damage_index = {
     "Training Sword": 10,
     "Steel Sword": 20,
     "Honed Blade": 35,
     "Master Sword": 50
}

spell_damage_index = {
     "Fireball": 25,
     "Ice Shards": 10,
     "Thunder Strike": 20,
     "Cursed Flames": 60,
     "Frost Blast": 30,
     "Lightning Storm": 50
}

spell_effect_index = {
     "Fireball": "Burned",
     "Ice Shards": "Frozen",
     "Thunder Strike": "Paralysed",
     "Cursed Flames": "Burned",
     "Frost Blast": "Frozen",
     "Lightning Storm": "Paralysed"
}

armor_reduction_index = {
     "No Armor": 0,
     "Leather Armor": 5,
     "Scale Mail": 10,
}

current_weapon = "Training Sword"
current_spell = "Thunder Strike"
current_armor = "No Armor"

player_damage = weapon_damage_index.get(current_weapon, 0)
player_spell_damage = spell_damage_index.get(current_spell, 0)
player_spell_effect = spell_effect_index.get(current_spell, 0)
player_armor_reduction = armor_reduction_index.get(current_armor, 0)

enemy_types = ["Bandit", "Wolf"]

enemy_stats_index = {
     "Bandit": {
        "hp_max": 4000,
        "hp_min": 3000,
        "damage_max": 10,
        "damage_min": 5,
        "accuracy": 95 
     },

     "Wolf": {
          "hp_max": 200,
          "hp_min": 199,
          "damage_max": 20,
          "damage_min": 10,
          "accuracy": 80
     },

}

healthbar_ui = ["[          ]","[-         ]","[--        ]","[---       ]","[----      ]","[-----     ]","[------    ]","[-------   ]","[--------  ]","[--------- ]", "[----------]"] 













def enemy_encounter(player_hp, player_max_hp, player_mana, player_max_mana):
    enemy = enemy_types[random.randint(0,1)]
    enemy_level = random.randint(1,3)
    enemy_stats = enemy_stats_index.get(enemy, {"hp_max": 1, "hp_min": 1, "damage_max": 1, "damage_min": 1, "accuracy": 1})
    enemy_max_hp = random.randint(enemy_stats["hp_min"], enemy_stats["hp_max"])
    enemy_hp = enemy_max_hp 
    enemy_debuff = "nil"
    
    turn = 1
    while enemy_hp > 0 and player_hp > 0: 
        
        print("\n--------------------------------------------------------\n")
        print("\nTurn {} \n".format(turn))
        
        # ui things 
        enemyhealthpercent = 100 * float(enemy_hp) / float(enemy_max_hp)
        enemy_ui_bar_index = min(int(enemyhealthpercent // 10), 10)
        playerhealthpercent = 100 * float(player_hp) / float(player_max_hp)
        player_ui_bar_index = min(int(playerhealthpercent // 10), 10)
        if enemy_debuff == "Burned" or enemy_debuff == "Frozen" or enemy_debuff == "Paralysed":
            print("{}({}): {} {}/{} \n \n{}: {} {}/{} \n".format(enemy, enemy_debuff, healthbar_ui[enemy_ui_bar_index], round(enemy_hp, 2), round(enemy_max_hp, 2), player_name, healthbar_ui[player_ui_bar_index], round(player_hp, 2), round(player_max_hp, 2)))
        else:
            print("{}: {} {}/{} \n \n{}: {} {}/{} \n".format(enemy, healthbar_ui[enemy_ui_bar_index], round(enemy_hp, 2), round(enemy_max_hp, 2), player_name, healthbar_ui[player_ui_bar_index], round(player_hp, 2), round(player_max_hp, 2)))
        
        
        decision = 0
        player_action_taken = False
        while player_action_taken == False:
            try: 
                decision = int(input("\nBattle Options: \n\n1. Weapon Attack ({})\n2. Mana Attack ({})\n3. Recover Mana\n4. Heal Wounds\n\nCurrent Mana: {}/{}\n\n".format(current_weapon, current_spell, player_mana, player_max_mana)))
            except ValueError:
                         print("Please enter a valid number!")
            else:
                if decision == 1: # attack
                    print("\nYou dealt {} damage to the opposing {} with your {}!".format(player_damage, enemy, current_weapon))
                    enemy_hp -= player_damage
                    mana_regen = True
                    player_action_taken = True
                
                elif decision == 2: # mana attack
                    if player_mana < 20:
                        print("\nYou do not have enough Mana (20 required) to successfully cast an attack spell.")
                    
                    else:
                        player_mana -= 20
                        effect_roll = random.randint(1,100)
                        if effect_roll <= 40:
                            print("\nYou dealt {} damage to the opposing {} with the {} spell! The {} is now {} (20 Mana expended).".format(player_spell_damage, enemy, current_spell, enemy, player_spell_effect.lower()))
                            enemy_hp -= player_spell_damage
                            enemy_debuff = player_spell_effect
                        else:
                            print("\nYou dealt {} damage to the opposing {} with a {}! (20 Mana expended)".format(player_spell_damage, enemy, current_spell))
                            enemy_hp -= player_spell_damage
                        mana_regen = False
                        player_action_taken = True

                elif decision == 3: # regen mana
                    print("\nYou spend the turn clearing your mind. You have recovered {} Mana.".format(player_max_mana * 0.5))
                    player_mana =  min(player_mana + player_max_mana * 0.5, player_max_mana)
                    mana_regen = False
                    player_action_taken = True
                
                elif decision == 4: # use a healing spell
                    ("\nYou cast a healing spell on yourself, recovering {} HP.".format(player_max_hp * 0.4))
                    player_hp = min(player_hp + player_max_hp * 0.4, player_max_hp)
                    mana_regen = False
                    player_action_taken = True
                else:
                    print("\nPlease enter a valid number!")
        
        #enemy's half of the turn

        if enemy_hp > 0:
            if enemy_debuff == "Paralysed" and random.randint(1,100) <= 25:
                print("The {} is paralysed! It cannot attack!".format(enemy))
            else:
                hit_roll = random.randint(1, 100)
                if hit_roll <=enemy_stats["accuracy"]: 
                    if enemy_debuff == "Frozen":
                        true_damage = random.randint(enemy_stats["damage_min"], enemy_stats["damage_max"])
                        damage_taken = max(0, ((true_damage - player_armor_reduction) * 0.5))
                        print("\nThe {} attacks you, with weakened attack power due to being frozen. You take {} damage.\n".format(enemy, round(damage_taken, 2)))
                        player_hp -= damage_taken
                    else:
                        true_damage = random.randint(enemy_stats["damage_min"], enemy_stats["damage_max"])
                        damage_taken = max(0, true_damage - player_armor_reduction)
                        print("\nThe {} attacks you. You take {} damage.\n".format(enemy, damage_taken))
                        player_hp -= damage_taken
                
                else:
                    print("\nThe {} attacks but misses!\n".format(enemy))
        

        # post-turn calculations 
        if enemy_debuff == "Burned":
            enemy_hp -= enemy_max_hp * 0.05
            print("The {} took {} damage from its burn.\n".format(enemy, round(enemy_max_hp * 0.05), 2))
        
        if mana_regen == True:
            player_mana = min(player_mana + player_max_mana * 0.1, player_max_mana)
            print("You naturally recover {} Mana at the end of your turn!".format(player_max_mana * 0.1))
        
        if enemy_debuff == "Burned" or enemy_debuff == "Frozen" or enemy_debuff == "Paralysed":
            if random.randint(1, 100) <= 75:
                print("\nThe {} failed to recover from its status effect!({})".format(enemy, enemy_debuff))
            else: 
                print("\nThe {} recovered from its status effect!({})".format(enemy, enemy_debuff))
                enemy_debuff = "nil"



        turn += 1
        
    # after battle end 

    if player_hp <= 0:
        print("{} has been defeated. Good Game!".format(player_name))
        quit()
    elif enemy_hp <= 0:
        print("{}: {} Defeated \n \n{}: {} {}/{} \n\nYou earned WIP EXP. Well Done! Returning to world map..".format(enemy, healthbar_ui[0], player_name, healthbar_ui[player_ui_bar_index], round(player_hp, 2), round(player_max_hp, 2)))
                 
                         




enemy_encounter(player_hp, player_max_hp, player_mana, player_max_mana)