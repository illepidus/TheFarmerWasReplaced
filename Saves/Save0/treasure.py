from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    plant(Entities.Bush)

    gold_before = num_items(Items.Gold)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    def shadow(gold0=gold_before):
        walk_left_hand(South, gold0)

    spawn_drone(shadow)
    walk_left_hand(North, gold_before)

def left_of(d):
    if d == North:
        return West
    if d == West:
        return South
    if d == South:
        return East
    return North

def right_of(d):
    if d == North:
        return East
    if d == East:
        return South
    if d == South:
        return West
    return North

def back_of(d):
    if d == North:
        return South
    if d == South:
        return North
    if d == East:
        return West
    return East

def walk_left_hand(direction, gold0):
    while num_items(Items.Gold) == gold0:
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True

        left = left_of(direction)

        if move(left):
            direction = left
        elif move(direction):
            pass
        else:
            right = right_of(direction)

            if move(right):
                direction = right
            else:
                direction = back_of(direction)
                move(direction)

    return False