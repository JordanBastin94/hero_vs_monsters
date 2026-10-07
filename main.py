from models.Human import Human
from models.Dwarf import Dwarf
from models.LittleDragon import LittleDragon
from models.Wolf import Wolf
from models.Orc import Orc
import random
import time

def choose_hero():
    choice = 0
    while choice not in ("1","2"):
        choice = input("Do you want to play as : 1.Human OR 2. Dwarf ? ")
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

def chooser_enemy():
    enemies = (Wolf(), Orc(), LittleDragon())
    enemy = random.choice(enemies)
    print(f"Enemy stats -> {enemy}")
    return enemy

def start_battle(hero, enemy):
    print("BATTLE BEGINS")
    while(hero.actual_hp > 0 and enemy.actual_hp >0):
        print("Hero attacks the enemy !")
        hero.strike(enemy)
        print(f"{enemy}")
        if enemy.actual_hp <=0 :
            print("Enemy is dead. YOU WON !")
            break
        time.sleep(2)
        print("Enemy attacks the hero !")
        enemy.strike(hero)
        print(f"{hero}")
        if hero.actual_hp <=0 :
            print("Hero is dead. YOU LOST !")
            break
        time.sleep(2)
    print("END OF BATTLE")

hero = choose_hero()
enemy = chooser_enemy()

input("Press enter to start the battle !")

start_battle(hero, enemy)