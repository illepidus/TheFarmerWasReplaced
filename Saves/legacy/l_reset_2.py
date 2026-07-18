import polyculture
import pumpkin_single
import treasure_single
import cactus
import bone_single

from l_reset_global import *


def pumpkin_until(x, y, target: int):
    while num_items(Items.Pumpkin) < target:
        pumpkin_single.cycle(x, y)


def bone_until(target: int):
    while num_items(Items.Bone) < target:
        bone_single.cycle()


def execute():
    clear()
    pumpkin_until(0, 0, 9000)
    unlock_or_throw(Unlocks.Expand)  # expand_5
    unlock_or_throw(Unlocks.Cactus)  # cactus_1
    unlock_or_throw(Unlocks.Polyculture)  # polyculture_1

    clear()
    polyculture.cycle(3, 3, Entities.Tree, (Items.Weird_Substance, 2000), True)
    unlock_or_throw(Unlocks.Mazes)  # mazes_1

    polyculture.cycle(3, 3, Entities.Carrot, (Items.Carrot, 200), True)

    clear()
    treasure_single.cycle(0, 0, 8, 2000)
    unlock_or_throw(Unlocks.Megafarm)  # megafarm_1

    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 62500))
    unlock_or_throw(Unlocks.Grass)  # grass_6

    polyculture.cycle(3, 3, Entities.Grass, (Items.Hay, 76800))
    unlock_or_throw(Unlocks.Trees)  # trees_6

    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 54000))
    unlock_or_throw(Unlocks.Fertilizer)  # fertilizer_4

    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 31200))
    unlock_or_throw(Unlocks.Carrots)  # carrots_5

    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 51200))
    unlock_or_throw(Unlocks.Watering)  # watering_6

    polyculture.cycle(3, 3, Entities.Carrot, (Items.Carrot, 5000))
    unlock_or_throw(Unlocks.Pumpkins)  # pumpkins_3

    pumpkin_until(0, 0, 1000)

    cactus.cycle(0, 0, 8, 8, True)
    unlock_or_throw(Unlocks.Dinosaurs)  # dinosaurs_1

    bone_until(10000)
    unlock_or_throw(Unlocks.Polyculture)  # polyculture_2

    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 312000))
    unlock_or_throw(Unlocks.Grass)  # grass_7

    polyculture.cycle(3, 3, Entities.Grass, (Items.Hay, 310000))
    unlock_or_throw(Unlocks.Trees)  # trees_7

    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 160000))
    unlock_or_throw(Unlocks.Carrots)  # carrots_6

    polyculture.cycle(3, 3, Entities.Carrot, (Items.Carrot, 18000))
    unlock_or_throw(Unlocks.Pumpkins)  # pumpkins_4

    pumpkin_until(0, 0, 8000)
    unlock_or_throw(Unlocks.Expand)  # expand_6

    spawn_drone(polyculture.cycle, 8, 8, Entities.Carrot, (Items.Carrot, 75000), True)
    polyculture.cycle(3, 3, Entities.Carrot, (Items.Carrot, 75000), True)
    unlock_or_throw(Unlocks.Pumpkins)  # pumpkins_5

    spawn_drone(pumpkin_until, 6, 6, 21000)
    pumpkin_until(0, 0, 21000)
    unlock_or_throw(Unlocks.Cactus)  # cactus_2

    clear()
    cactus.cycle(0, 0, 12, 12, True)
    unlock_or_throw(Unlocks.Mazes)  # mazes_2
    unlock_or_throw(Unlocks.Dinosaurs)  # dinosaurs_2

    clear()
    treasure_single.cycle(0, 0, 6, 8000)
    unlock_or_throw(Unlocks.Megafarm)  # megafarm_2

    clear()
    spawn_drone(polyculture.cycle, 8, 8, Entities.Tree, (Items.Wood, 800000), True)
    polyculture.cycle(3, 3, Entities.Tree, (Items.Wood, 800000), True)
    unlock_or_throw(Unlocks.Carrots)  # carrots_7

    clear()
    spawn_drone(polyculture.cycle, 8, 8, Entities.Carrot, (Items.Carrot, 325000), True)
    polyculture.cycle(3, 3, Entities.Carrot, (Items.Carrot, 325000), True)
    unlock_or_throw(Unlocks.Pumpkins)  # pumpkins_7

    clear()
    spawn_drone(pumpkin_until, 6, 6, 64000)
    pumpkin_until(0, 0, 64000)
    unlock_or_throw(Unlocks.Expand)  # expand_7

    clear()
    spawn_drone(pumpkin_until, 0, 0, 130000)
    spawn_drone(pumpkin_until, 7, 0, 130000)
    spawn_drone(pumpkin_until, 0, 7, 130000)
    spawn_drone(pumpkin_until, 7, 7, 130000)
    pumpkin_until(7, 7, 130000)
    unlock_or_throw(Unlocks.Cactus)  # cactus_3

    clear()
    cactus.cycle(0, 0, 16, 16, True)
    unlock_or_throw(Unlocks.Mazes)  # mazes_3
    unlock_or_throw(Unlocks.Dinosaurs)  # dinosaurs_3

    infinite_loop()
