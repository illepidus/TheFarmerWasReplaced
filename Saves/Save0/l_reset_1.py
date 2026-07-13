from __builtins__ import *

_T0_ = get_time()


def infinite_loop():
    def _f():
        return

    while True:
        _f()

def throw_exception(text: string):
    quick_print("exception:", text)
    _ = 0 / 0


def unlock_or_throw(u):
    if unlock(u):
        lvl = num_unlocked(u)
        cost = get_cost(u, lvl - 1)
        quick_print(get_time() - _T0_, "Unlocked", u, "lvl", lvl, "for", cost)
    else:
        throw_exception("Was not able to unlock " + str(u))



def execute():
    while num_items(Items.Hay) < 20:
        harvest()

    unlock_or_throw(Unlocks.Speed)  # speed_1

    while num_items(Items.Hay) < 30:
        if can_harvest():
            harvest()

    unlock_or_throw(Unlocks.Expand)  # expand_1

    while num_items(Items.Hay) < 100:
        if can_harvest():
            harvest()

    unlock_or_throw(Unlocks.Plant)  # plants_1

    while num_items(Items.Wood) < 20:
        if can_harvest():
            harvest()
            plant(Entities.Bush)
        move(North)
    unlock_or_throw(Unlocks.Expand)  # expand_2

    while num_items(Items.Wood) < 20:
        for _ in range(3):
            for _ in range(3):
                if can_harvest():
                    harvest()
                    plant(Entities.Bush)
                move(East)
            move(North)
    unlock_or_throw(Unlocks.Speed)  # speed_2

    while num_items(Items.Wood) < 50:
        for _ in range(3):
            for _ in range(3):
                if can_harvest():
                    harvest()
                    plant(Entities.Bush)
                move(East)
            move(North)
    unlock_or_throw(Unlocks.Carrots)  # carrots_1

    while num_items(Items.Wood) < 50 or num_items(Items.Carrot) < 90:
        for i in range(3):
            for j in range(3):
                if can_harvest():
                    harvest()
                    if (i * 3 + j) < 5:
                        plant(Entities.Bush)
                    else:
                        if get_ground_type() == Grounds.Grassland:
                            till()
                        plant(Entities.Carrot)
                move(East)
            move(North)
    unlock_or_throw(Unlocks.Trees)  # trees_1

    clear()
    while num_items(Items.Wood) < 80:
        for i in range(3):
            for j in range(3):
                if can_harvest():
                    harvest()
                    if (i + j) % 2 == 0:
                        plant(Entities.Tree)
                move(East)
            move(North)
    unlock_or_throw(Unlocks.Watering)  # watering_1
    unlock_or_throw(Unlocks.Expand)  # expand_3

    while num_items(Items.Wood) < 1200 or num_items(Items.Hay) < 350:
        for i in range(4):
            for j in range(4):
                if can_harvest():
                    harvest()
                    if (i + j) % 2 == 0:
                        plant(Entities.Tree)
                move(East)
            move(North)
    unlock_or_throw(Unlocks.Carrots)  # carrots_2
    unlock_or_throw(Unlocks.Grass)  # grass_2
    unlock_or_throw(Unlocks.Grass)  # grass_3
    unlock_or_throw(Unlocks.Watering)  # watering_2

    while num_items(Items.Carrot) < 100 or num_items(Items.Hay) < 300:
        for i in range(4):
            for j in range(4):
                if can_harvest():
                    harvest()
                    if (i + j) % 2 == 0:
                        if get_ground_type() == Grounds.Grassland:
                            till()
                        plant(Entities.Carrot)
                move(East)
            move(North)
    unlock_or_throw(Unlocks.Speed)  # speed_3
    unlock_or_throw(Unlocks.Trees)  # trees_2
    unlock_or_throw(Unlocks.Expand)  # expand_4

    clear()
    def wood_hay6():
        for i in range(6):
            for j in range(6):
                if can_harvest():
                    harvest()
                    if (i + j) % 2 == 0:
                        plant(Entities.Tree)
                move(East)
            move(North)

    while num_items(Items.Wood) < 2500 or num_items(Items.Hay) < 1200:
        wood_hay6()
    unlock_or_throw(Unlocks.Trees)  # trees_3
    unlock_or_throw(Unlocks.Grass)  # grass_4

    while num_items(Items.Wood) < 5000:
        wood_hay6()
    unlock_or_throw(Unlocks.Watering)  # watering_3
    unlock_or_throw(Unlocks.Carrots)  # carrots_3

    def till_6():
        for _ in range(6):
            for _ in range(6):
                till()
                plant(Entities.Carrot)
                move(East)
            move(North)

    def carrot6():
        for _ in range(6):
            for _ in range(6):
                if can_harvest():
                    harvest()
                    plant(Entities.Carrot)
                move(East)
            move(North)

    clear()
    till_6()
    while num_items(Items.Carrot) < 500:
        carrot6()
    unlock_or_throw(Unlocks.Speed)  # speed_4

    while num_items(Items.Carrot) < 1000:
        carrot6()
    unlock_or_throw(Unlocks.Speed)  # speed_5

    clear()
    while num_items(Items.Hay) < 5000:
        for _ in range(6):
            for _ in range(6):
                if can_harvest():
                    harvest()
                move(East)
        move(North)
    unlock_or_throw(Unlocks.Trees) # trees_4

    while num_items(Items.Wood) < 3200:
        wood_hay6()
    unlock_or_throw(Unlocks.Watering) # watering_4

    while num_items(Items.Wood) < 12500:
        wood_hay6()
    unlock_or_throw(Unlocks.Grass) # grass_6

    while num_items(Items.Wood) < 7500:
        wood_hay6()
    unlock_or_throw(Unlocks.Carrots) # carrots_4
    unlock_or_throw(Unlocks.Hats) # hats_1

    clear()
    till_6()
    while num_items(Items.Carrot) < 700:
        carrot6()
    unlock_or_throw(Unlocks.Sunflowers) # sunflowers_1

    def balanced6():
        for i in range(6):
            for j in range(6):
                if can_harvest():
                    harvest()
                    if (i * 6 + j) > 30:
                        if get_ground_type() == Grounds.Grassland:
                            till()
                        plant(Entities.Carrot)
                    elif (i + j) % 3 == 0:
                        if get_ground_type() == Grounds.Grassland:
                            till()
                        plant(Entities.Sunflower)
                    elif (i + j) % 2 == 0:
                        plant(Entities.Tree)
                move(East)
            move(North)

    clear()
    while num_items(Items.Power) < 100 or num_items(Items.Carrot) < 200:
        balanced6()
    unlock_or_throw(Unlocks.Pumpkins)


    infinite_loop()