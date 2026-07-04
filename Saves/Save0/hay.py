from __builtins__ import *
import move
import water


def cycle(x0=0, y0=0, s=get_world_size()):
    change_hat(Hats.Gray_Hat)
    for x in range(s):
        for y in range(s):
            move.to(x + x0, y + y0)

            if get_ground_type() != Grounds.Grassland:
                till()
            if get_entity_type() != Entities.Grass:
                harvest()
            elif can_harvest():
                harvest()
            else:
                water.apply() # do not think this ever happens
