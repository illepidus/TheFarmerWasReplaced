from l_reset_global import *
import pumpkin_single
import polyculture

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

    polyculture.cycle(3,3, Entities.Tree, (Items.Wood, 31200), True)
    unlock_or_throw(Unlocks.Carrots) # carrots_5

    polyculture.cycle(3,3, Entities.Tree, (Items.Wood, 51200), True)
    unlock_or_throw(Unlocks.Watering) # watering_6

    infinite_loop()