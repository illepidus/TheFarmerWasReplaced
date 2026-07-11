from __builtins__ import *
from _movement import fly


def _init(p0, size):
    fly(p0)

    plan = []
    for i in range(size):
        if i != 0:
            plan.append(North)
        for _ in range(size - 1):
            if i % 2 == 0:
                plan.append(East)
            else:
                plan.append(West)

    def _plant():
        if get_ground_type() != Grounds.Soil:  # no pumpkins can grow here
            till()

        if get_entity_type() != Entities.Pumpkin:  # not a pumpkin
            harvest()
            plant(Entities.Pumpkin)

    for direction in plan:
        _plant()
        move(direction)
    _plant()

def _first_run(p0, size):
    queue = list()
    for i in range(size):
        for j in range(size):
            fly((p0[0] + i, p0[1] + j))

            entity = get_entity_type()

            if entity == Entities.Dead_Pumpkin or not can_harvest():
                if entity == Entities.Dead_Pumpkin:
                    harvest()
                    plant(Entities.Pumpkin)

                queue.append((p0[0] + i, p0[1] + j))
                while get_water() < 0.75:
                    use_item(Items.Water)

    return queue


def cycle(x0=0, y0=0, s=6):
    change_hat(Hats.Pumpkin_Hat)
    _init((x0, y0), s)
    queue = _first_run((x0, y0), s)

    while len(queue) > 0:
        task = queue.pop(0)
        fly(task)

        if get_entity_type() == Entities.Dead_Pumpkin:  # dead pumpkin
            harvest()
            plant(Entities.Pumpkin)
            while get_water() < 0.75:
                use_item(Items.Water)
            queue.append(task)
        elif not can_harvest():  # still not grown pumpkin, let's move to next one
            queue.append(task)

    harvest()
