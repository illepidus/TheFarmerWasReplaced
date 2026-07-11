from __builtins__ import *
from _movement import fly


def _init(p0, size):
    queue = list()
    for i in range(size):
        for j in range(size):
            queue.append((p0[0] + i, p0[1] + j))
    return queue

def cycle(x0=0, y0=0, s=6):
    change_hat(Hats.Pumpkin_Hat)
    queue = _init((x0, y0), s)

    while len(queue) > 0:
        task = queue.pop(0)
        fly(task)

        if get_ground_type() != Grounds.Soil:  # no pumpkins can grow here
            till()

        if get_entity_type() != Entities.Pumpkin:  # dead pumpkin / not a pumpkin
            harvest()
            plant(Entities.Pumpkin)
            queue.append(task)
        elif not can_harvest():  # still not grown pumpkin, let's move to next one
            queue.append(task)

    harvest()


cycle(0, 0, 32)
