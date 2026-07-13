from __builtins__ import *
import move


def cycle(x=0, y=0, target=64):
    clear()
    change_hat(Hats.Carrot_Hat)
    move.to(x, y)
    i = 0
    if get_ground_type() != Grounds.Soil:
        till()
    if get_entity_type() != Entities.Carrot:
        plant(Entities.Carrot)

    while True:
        if i >= target:
            break

        if can_harvest():
            harvest()
            plant(Entities.Carrot)
            i += 1
        else:
            use_item(Items.Fertilizer)

    clear()