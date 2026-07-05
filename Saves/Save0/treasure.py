from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    change_hat(Hats.Purple_Hat)

    gold0 = num_items(Items.Gold)

    # Расставляем spawned-дронов до появления лабиринта.
    scatter_drones(s, gold0)

    # Не возвращаемся в 0,0.
    # Создаём лабиринт там, где главный дрон оказался после расстановки.
    plant(Entities.Bush)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    # Главный дрон тоже участвует из текущей позиции.
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

def go_to(tx, ty):
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
    # Всего хотим использовать до max_drones().
    # Один дрон — текущий, поэтому spawn'им максимум max_drones() - 1.
    spawn_limit = max_drones() - 1

    # Не больше, чем клеток кроме текущей.
    max_by_field = s * s - 1

    if spawn_limit > max_by_field:
        spawn_limit = max_by_field

    if spawn_limit <= 0:
        return

    # Квадратная сетка k x k, потому что поле s x s.
    #
    # Для 32 дронов:
    # spawned = 31
    # k = 6
    # точки будут лежать примерно в центрах 6x6 секторов.
    k = ceil_sqrt(spawn_limit + 1)

    spawned = 0
    row = 0

    while row < k and spawned < spawn_limit:
        if row % 2 == 0:
            col = 0

            while col < k and spawned < spawn_limit:
                spawned = scatter_one(row, col, k, spawned, gold0, s)
                col = col + 1
        else:
            col = k - 1

            while col >= 0 and spawned < spawn_limit:
                spawned = scatter_one(row, col, k, spawned, gold0, s)
                col = col - 1

        row = row + 1

def scatter_one(row, col, k, spawned, gold0, s):
    # Центр сектора квадратной сетки.
    x = ((2 * col + 1) * s) // (2 * k)
    y = ((2 * row + 1) * s) // (2 * k)

    # Если сектор попал в текущую/стартовую клетку, можно всё равно спавнить:
    # это не критично, но обычно для s=31 и k>=2 сюда не попадём.
    go_to(x, y)

    drone = spawn_drone(
        walk_left,
        direction_for(spawned + 1),
        gold0,
        s
    )

    if drone == None:
        return spawned

    return spawned + 1