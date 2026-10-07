from models.Human import Human
from models.Dwarf import Dwarf
from models.LittleDragon import LittleDragon
from models.Wolf import Wolf
from models.Orc import Orc


orc = Orc()
wolf = Wolf()
ld = LittleDragon()
dwarf = Dwarf()
human = Human()

print("Human = ","STR - ",human.str,"END - ", human.end,"MAX-HP - ", human.max_hp,"actual-HP - ", human.actual_hp, "gold amount : ", human.gold_stock, "leather_amonut : ", human.leather_stock, "bonus STR : ", human.bonus_str, "Bonus END : ", human.bonus_end)
print("dwarf = ","STR - ",dwarf.str,"END - ", dwarf.end,"MAX-HP - ", dwarf.max_hp,"actual-HP - ", dwarf.actual_hp, "gold amount : ", dwarf.gold_stock, "leather_amonut : ", dwarf.leather_stock, "bonus STR : ", dwarf.bonus_str, "bonus End : ", dwarf.bonus_end)
print("little_dragon = ","STR - ",ld.str,"END - ", ld.end,"MAX-HP - ", ld.max_hp,"actual-HP - ", ld.actual_hp, "gold amount : ", ld.gold_amount, "leather_amonut : ", ld.leather_amount, "bonus STR : ", ld.bonus_str, "Bonus END : ", ld.bonus_end)
print("wolf = ","STR - ",wolf.str,"END - ", wolf.end,"MAX-HP - ", wolf.max_hp,"actual-HP - ", wolf.actual_hp, "gold amount : ", wolf.gold_amount, "leather_amonut : ", wolf.leather_amount, "Bonus STR : ", wolf.bonus_str, "Bonus END : ", wolf.bonus_end)
print("orc = ","STR - ",orc.str,"END - ", orc.end,"MAX-HP - ", orc.max_hp,"actual-HP - ", orc.actual_hp,  "gold amount : ", orc.gold_amount, "leather_amonut : ", orc.leather_amount, "Bonus STR : ", orc.bonus_str, "Bonus END : ", orc.bonus_end)

print("------------------------COMBAT")
print("actual-HP - ", orc.actual_hp)
human.strike(orc)
print("actual-HP - ", orc.actual_hp)

print("actual-HP - ", human.actual_hp)
orc.strike(human)
print("actual-HP - ", human.actual_hp)
human.regenerate_hp()
print("actual-HP - ", human.actual_hp)


print("actual gold : ", human.gold_stock)
human.loot_monster(orc)
print("actual gold : ", human.gold_stock)