from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    plant(Entities.Bush)
    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
    step(North)

def step(direction: Direction):
    if direction == North:
        plan = [West, North, East, South]
    elif direction == West:
        plan = [South, West, North, East]
    elif direction == South:
        plan = [East, South, West, North]
    else:
        plan = [North, East, South, North]

    for direction in plan:
        if move(direction):
            if get_entity_type() == Entities.Treasure:
                harvest()
                return True
            else:
                if step(direction):
                    return True

    return False
