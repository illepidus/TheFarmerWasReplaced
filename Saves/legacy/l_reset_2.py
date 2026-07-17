import polyculture
import pumpkin_single
import treasure_single
import cactus


from l_reset_global import *


def execute():
    clear()
    while num_items(Items.Pumpkin) < 9000:
        pumpkin_single.cycle(0, 0, 6)
    unlock_or_throw(Unlocks.Expand) # expand_5
    unlock_or_throw(Unlocks.Cactus) # cactus_1
    unlock_or_throw(Unlocks.Polyculture) # polyculture_1

    polyculture.cycle(3,3, Entities.Tree, (Items.Wood, 62500), True)
    unlock_or_throw(Unlocks.Grass) # grass_6

    polyculture.cycle(3,3, Entities.Grass, (Items.Hay, 76800), True)
    unlock_or_throw(Unlocks.Trees) # trees_6

    polyculture.cycle(3,3, Entities.Tree, (Items.Wood, 54000), True)
    unlock_or_throw(Unlocks.Fertilizer) # fertilizer_4

    polyculture.cycle(3,3, Entities.Tree, (Items.Wood, 31200), True)
    unlock_or_throw(Unlocks.Carrots) # carrots_5

    polyculture.cycle(3,3, Entities.Tree, (Items.Wood, 51200), True)
    unlock_or_throw(Unlocks.Watering) # watering_6

    polyculture.cycle(3,3, Entities.Tree, (Items.Weird_Substance, 1000), True)
    unlock_or_throw(Unlocks.Mazes) # mazes_1

    clear()
    treasure_single.cycle(0, 0, 8, 2000)
    unlock_or_throw(Unlocks.Megafarm) # megafarm_1

    polyculture.cycle(3,3, Entities.Tree, (Items.Carrot, 5000), False)
    unlock_or_throw(Unlocks.Pumpkins) # pumpkins_3

    while num_items(Items.Pumpkin) < 1000:
        pumpkin_single.cycle(0, 0, 6)

    cactus.cycle(0, 0, 8, 8, True)


    infinite_loop()