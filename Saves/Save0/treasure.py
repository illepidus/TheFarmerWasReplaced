from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    plant(Entities.Bush)

    gold = num_items(Items.Gold)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    def shadow(before=gold):
        walk_hand(North, False, before) # right hand

    spawn_drone(shadow)
    walk_hand(North, True, gold) # left hand

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

def walk_hand(direction, left_hand, gold0):
    while num_items(Items.Gold) == gold0:
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True

        if left_hand:
            first = left_of(direction)
            third = right_of(direction)
        else:
            first = right_of(direction)
            third = left_of(direction)

        if move(first):
            direction = first
        elif move(direction):
            pass
        elif move(third):
            direction = third
        else:
            direction = back_of(direction)
            move(direction)

    return False