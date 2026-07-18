from l_reset_global import *
import treasure_single
import cactus
import bone_single


def execute():
    clear()
    for i in range(2):
        for j in range(2):
            if i != 0 or j != 0:
                spawn_drone(treasure_single.cycle, i, j, 5, 32000, 1)

    treasure_single.cycle(0, 0, 5, 32000, 5)
    unlock_or_throw(Unlocks.Megafarm)  # megafarm_3

    clear()
    for i in range(3):
        for j in range(3):
            if i != 0 or j != 0:
                spawn_drone(treasure_single.cycle, i, j, 5, 128000, 1)

    treasure_single.cycle(0, 0, 5, 128000, 5)
    unlock_or_throw(Unlocks.Megafarm)  # megafarm_4

    clear()
    while num_items(Items.Cactus) < 432000:
        cactus.cycle(0, 0, 16, 16)
    unlock_or_throw(Unlocks.Mazes)  # mazes_4

    set_world_size(12)
    bone_single.cycle()
    unlock_or_throw(Unlocks.Polyculture)  # polyculture_3
    set_world_size(16)

    infinite_loop()
