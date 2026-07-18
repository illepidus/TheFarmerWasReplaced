from _farming import *
from _movement import *


def plant_and_scout() -> dict[int, list[tuple[int, int]]]:
    ws = get_world_size()
    fly((0, 0))

    data = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
    for j in range(ws):
        for i in range(ws):
            smart_plant(Entities.Sunflower)
            m = measure()
            if m in data:
                append(data[m], (i, j))
            else:
                data[m] = [(i, j)]
            if m < 10 and get_water() < 0.5:
                use_item(Items.Water, 2)
            move(East)
        move(North)

    return data


def cycle(until: int | None = None):
    finished = False

    if until != None:
        if num_items(Items.Power) >= until:
            finished = True

    while not finished:
        if until != None:
            if num_items(Items.Power) >= until:
                finished = True

        data = plant_and_scout()

        for petals in data:
            for coord in data[petals]:
                fly(coord)
                while not can_harvest():
                    if get_water() < 0.75:
                        use_item(Items.Water)
                harvest()
