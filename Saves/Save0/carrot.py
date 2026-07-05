from __builtins__ import *
import move
import water


def cycle(x0=0, y0=0, s=min(8, get_world_size())):
    change_hat(Hats.Carrot_Hat)
    for x in range(s):
        for y in range(s):
            move.to(x + x0, y + y0)

            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != Entities.Carrot or can_harvest():
                harvest()
                plant(Entities.Carrot)
            else:
                water.apply()
