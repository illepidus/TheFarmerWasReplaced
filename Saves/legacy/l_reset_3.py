from l_reset_global import *
import treasure_single
import cactus
import bone_single
import polyculture
import pumpkin_single


def pumpkin_until(x, y, target: int):
    while num_items(Items.Pumpkin) < target:
        pumpkin_single.cycle(x, y)


def execute():
    clear()
    for i in range(2):
        for j in range(2):
            if i != 0 or j != 0:
                spawn_drone(treasure_single.cycle, i, j, 5, 32000, 1)

    treasure_single.cycle(0, 0, 5, 32000, 1)
    unlock_or_throw(Unlocks.Megafarm)  # megafarm_3

    clear()
    for i in range(3):
        for j in range(3):
            if i != 0 or j != 0:
                spawn_drone(treasure_single.cycle, i, j, 5, 128000, 1)

    treasure_single.cycle(0, 0, 5, 128000, 1)
    unlock_or_throw(Unlocks.Megafarm)  # megafarm_4

    clear()
    while num_items(Items.Cactus) < 432000:
        cactus.cycle(0, 0, 16, 16)
    unlock_or_throw(Unlocks.Mazes)  # mazes_4

    set_world_size(12)
    bone_single.cycle()
    unlock_or_throw(Unlocks.Polyculture)  # polyculture_3
    set_world_size(16)

    clear()
    spawn_drone(polyculture.cycle, 11, 3, Entities.Carrot, (Items.Carrot, 1250000))
    spawn_drone(polyculture.cycle, 3, 11, Entities.Carrot, (Items.Carrot, 1250000))
    spawn_drone(polyculture.cycle, 11, 11, Entities.Carrot, (Items.Carrot, 1250000))
    polyculture.cycle(3, 3, Entities.Carrot, (Items.Carrot, 1250000))
    unlock_or_throw(Unlocks.Pumpkins)  # pumkins_7

    clear()
    spawn_drone(pumpkin_until, 0, 0, 800000)
    spawn_drone(pumpkin_until, 7, 0, 800000)
    spawn_drone(pumpkin_until, 0, 7, 800000)
    pumpkin_until(7, 7, 800000)
    unlock_or_throw(Unlocks.Cactus)  # cactus_4

    clear()
    while num_items(Items.Cactus) < 2590000 * 2 + 432000 + 200000:
        cactus.cycle(0, 0, 16, 16)
    unlock_or_throw(Unlocks.Dinosaurs)  # dinosaurs_4
    unlock_or_throw(Unlocks.Dinosaurs)  # dinosaurs_5
    unlock_or_throw(Unlocks.Mazes)  # mazes_5

    bone_single.cycle()
    bone_single.cycle()

    clear()
    for i in range(4):
        for j in range(4):
            if i != 0 or j != 0:
                spawn_drone(treasure_single.cycle, i, j, 4, 1000000, 2)

    treasure_single.cycle(0, 0, 4, 1000000, 2)
    unlock_or_throw(Unlocks.Leaderboard)
