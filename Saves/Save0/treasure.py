from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    change_hat(Hats.Purple_Hat)

    gold0 = num_items(Items.Gold)
    scatter_drones(s, gold0)

    plant(Entities.Bush)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    walk_left(North, gold0, s)

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

def direction_for(i):
    r = i % 4

    if r == 0:
        return North
    if r == 1:
        return East
    if r == 2:
        return South

    return West

def ceil_sqrt(n):
    r = 1

    while r * r < n:
        r = r + 1

    return r

def points_in_row(row, rows, total):
    return ((row + 1) * total) // rows - (row * total) // rows

def go_to(tx, ty):
    while get_pos_x() < tx:
        move(East)

    while get_pos_x() > tx:
        move(West)

    while get_pos_y() < ty:
        move(North)

    while get_pos_y() > ty:
        move(South)

def go_to_point(row, index_in_row, rows, count_in_row, s):
    y = ((2 * row + 1) * s) // (2 * rows)
    x = ((2 * index_in_row + 1) * s) // (2 * count_in_row)

    go_to(x, y)

def can_go(direction, s):
    x = get_pos_x()
    y = get_pos_y()

    if direction == East and x >= s - 1:
        return False

    if direction == West and x <= 0:
        return False

    if direction == North and y >= s - 1:
        return False

    if direction == South and y <= 0:
        return False

    return can_move(direction)

def walk_left(direction, gold0, s):
    while num_items(Items.Gold) == gold0:
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True

        left = left_of(direction)
        right = right_of(direction)

        if can_go(left, s):
            move(left)
            direction = left
        elif can_go(direction, s):
            move(direction)
        elif can_go(right, s):
            move(right)
            direction = right
        else:
            direction = back_of(direction)

            if can_go(direction, s):
                move(direction)
            else:
                return False

    return False

def scatter_drones(s, gold0):
    total = max_drones()

    if total > s * s:
        total = s * s

    if total <= 1:
        return

    rows = ceil_sqrt(total)

    placed = 0
    row = 0

    while row < rows and placed < total:
        count = points_in_row(row, rows, total)

        if row % 2 == 0:
            i = 0

            while i < count and placed < total:
                go_to_point(row, i, rows, count, s)
                placed = place_drone_or_master(placed, total, gold0, s)
                i = i + 1
        else:
            i = count - 1

            while i >= 0 and placed < total:
                go_to_point(row, i, rows, count, s)
                placed = place_drone_or_master(placed, total, gold0, s)
                i = i - 1

        row = row + 1

def place_drone_or_master(placed, total, gold0, s):
    # Последняя точка остаётся мастеру.
    if placed == total - 1:
        return total

    drone = spawn_drone(
        walk_left,
        direction_for(placed + 1),
        gold0,
        s
    )

    if drone == None:
        return total

    return placed + 1