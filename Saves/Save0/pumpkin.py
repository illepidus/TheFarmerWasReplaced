from __builtins__ import *
from _movement import fly
from _farming import smart_plant


def _cycle(p: tuple[int, int]):
    fly(p)
    smart_plant(Entities.Pumpkin)
    while True:
        if can_harvest():
            harvest()
            plant(Entities.Pumpkin)
        elif get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)
        elif get_water() < 0.75:
            use_item(Items.Water)
        else:
            use_item(Items.Fertilizer)


ws = get_world_size()
clear()

def cycle(p: tuple[int, int]):
    for i in range(6):
        for j in range(6):
            if i != 0 or j != 0:
                if num_drones() < max_drones():
                    spawn_drone(_cycle, (p[0] + i, p[0] + j), ws)
                else:
                    return

cycle((0, 0))
_cycle((0, 0), ws)
