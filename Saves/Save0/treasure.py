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

def go_to(tx, ty, s):
    # Важно: не используем wrap через край мира.
    # Двигаемся только внутри квадрата 0..s-1.

    while get_pos_x() < tx:
        move(East)

    while get_pos_x() > tx:
        move(West)

    while get_pos_y() < ty:
        move(North)

    while get_pos_y() > ty:
        move(South)

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
    spawn_count = max_drones() - 1

    # Нет смысла пытаться занять больше разных стартовых клеток,
    # чем есть в квадрате s*s. Одну клетку оставляем основному дрону.
    max_spawn_count = s * s - 1

    if spawn_count > max_spawn_count:
        spawn_count = max_spawn_count

    if spawn_count <= 0:
        return

    cols = ceil_sqrt(spawn_count)
    rows = (spawn_count + cols - 1) // cols

    spawned = 0
    row = 0

    while row < rows and spawned < spawn_count:
        if row % 2 == 0:
            col = 0

            while col < cols and spawned < spawn_count:
                spawned = scatter_one(row, col, rows, cols, spawned, gold0, s)
                col = col + 1
        else:
            col = cols - 1

            while col >= 0 and spawned < spawn_count:
                spawned = scatter_one(row, col, rows, cols, spawned, gold0, s)
                col = col - 1

        row = row + 1

def scatter_one(row, col, rows, cols, spawned, gold0, s):
    # Центр сектора сетки.
    x = ((2 * col + 1) * s) // (2 * cols)
    y = ((2 * row + 1) * s) // (2 * rows)

    # Теоретически для маленьких s можно попасть в 0,0.
    # Там потом будет основной дрон, так что эту точку пропускаем.
    if x == 0 and y == 0:
        return spawned

    go_to(x, y, s)

    drone = spawn_drone(
        walk_left,
        direction_for(spawned + 1),
        gold0,
        s
    )

    if drone == None:
        return spawned

    return spawned + 1