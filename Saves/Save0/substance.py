from __builtins__ import *


def cycle():
    if get_ground_type() != Grounds.Soil:
        till()
    if get_entity_type() != Entities.Carrot:
        plant(Entities.Carrot)

    while True:
        if can_harvest():
            harvest()
            plant(Entities.Carrot)
        else:
            use_item(Items.Fertilizer)
