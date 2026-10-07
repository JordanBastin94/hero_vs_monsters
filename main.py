from models.Human import Human
from models.Dwarf import Dwarf
from models.LittleDragon import LittleDragon
from models.Wolf import Wolf
from models.Orc import Orc
from models.Hero import Hero
from models.Monster import Monster
import random
import time

def choose_hero() -> Hero:
    choice = ""
    while choice not in ("1","2"):
        choice = input("Do you want to play as :\n1. Human OR 2. Dwarf ? ")
        if choice == "1" :
            print("You have chosen the Human race !")
            hero = Human()
        elif choice == "2":
            print("You have chosen the Dwarf race !")
            hero = Dwarf()
        else :
            print("juste choose 1 OR 2 ! It's not that complicated ...")
    print(f"Hero stats -> {hero}")
    return hero

def chooser_enemy() -> Monster:
    enemies = (Wolf, Orc, LittleDragon)
    enemy = random.choice(enemies)
    enemy = enemy()
    print(f"Enemy stats -> {enemy}")
    return enemy

def start_battle(hero:Hero, enemy:Monster):
    print("----------BATTLE BEGINS----------")
    while(hero.is_alive and enemy.is_alive):
        #Hero's turn
        print("Hero attacks the enemy !")
        hero.strike(enemy)
        print(f"Enemy's actual hp : {enemy.actual_hp}")
        if not enemy.is_alive :
            print("Enemy is dead. YOU WON !")
            hero.loot_monster(enemy)
            print(f"Hero's inventory - Gold : {hero.gold_stock}, Leather : {hero.leather_stock}")
            break
        time.sleep(2)

        #Enemy's turn
        print("Enemy attacks the hero !")
        enemy.strike(hero)
        print(f"Hero's actual hp : {hero.actual_hp}")
        if not hero.is_alive :
            print("Hero is dead. YOU LOST !")
            break
        time.sleep(2)
        print("--------------------------------------")
    print("END OF BATTLE")
    print("--------------------------------------")

hero = choose_hero()
while hero.is_alive :
    enemy = chooser_enemy()
    input("Press enter to start the battle !")
    start_battle(hero, enemy)
    if hero.is_alive :
        print("Good job ! You won your battle !")
        hero.regenerate_hp()
    else :
        print("Hero is dead ! Monster wins")