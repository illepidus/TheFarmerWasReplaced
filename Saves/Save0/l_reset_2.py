from l_reset_global import *
import pumpkin_single

def execute():
    clear()
    while num_items(Items.Pumpkin) < 9000:
        pumpkin_single.cycle(0, 0, 6)
    unlock_or_throw(Unlocks.Expand) # expand_5
    unlock_or_throw(Unlocks.Cactus) # cactus
    unlock_or_throw(Unlocks.Polyculture) # polyculture

    infinite_loop()