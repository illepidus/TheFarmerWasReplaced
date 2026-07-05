from __builtins__ import *
import move
import water


def _init(size):
    field = []
    v = 1
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(v)
            v += 1
        field.append(row)
    return field, v


def _find_min(field):
    min_x = 0
    min_y = 0
    min_v = None

    for y in range(len(field)):
        for x in range(len(field[y])):
            v = field[y][x]
            if v != 0:
                if min_v == None or v < min_v:
                    min_v = v
                    min_x = x
                    min_y = y

    return min_x, min_y, min_v


def cycle(x0=0, y0=0, s=min(6, get_world_size())):
    change_hat(Hats.Pumpkin_Hat)

    field, next_v = _init(s)

    while True:
        x, y, v = _find_min(field)
        if v == None:
            break

        move.to(x + x0, y + y0)

        if get_ground_type() != Grounds.Soil:  # no pumpkins can grow here
            till()

        if get_entity_type() != Entities.Pumpkin:  # dead pumpkin / not a pumpkin
            harvest()
            water.apply()
            plant(Entities.Pumpkin)
            field[y][x] = next_v
            next_v += 1
        elif can_harvest():  # nice! this pumpkin is nice and grown lets forget about it
            field[y][x] = 0
        else:  # still not grown pumpkin, let's move to next one
            water.apply()
            field[y][x] = next_v
            next_v += 1

    harvest()
