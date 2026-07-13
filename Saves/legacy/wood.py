from __builtins__ import *
import move
import water


def cycle(x0=0, y0=0, s=min(8, get_world_size())):
    change_hat(Hats.Green_Hat)
    for x in range(s):
        for y in range(s):
            move.to(x + x0, y + y0)

            if get_entity_type() not in (Entities.Tree, Entities.Bush) or can_harvest():
                harvest()
                if (x + y) % 2 == 0:
                    plant(Entities.Tree)
                else:
                    plant(Entities.Bush)
            else:
                water.apply()
