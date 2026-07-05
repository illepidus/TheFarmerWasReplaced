from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    change_hat(Hats.Purple_Hat)

    gold0 = num_items(Items.Gold)

    # До появления лабиринта расставляем дронов.
    # Spawned-дроны НЕ ходят, а ждут measure() != None.
    # Последняя точка раскладки остаётся мастеру.
    scatter_drones(s, gold0)

    # Лабиринт появляется здесь.
    plant(Entities.Bush)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    # Мастер тоже участвует из своей текущей позиции.
    walk_left(North, gold0, s)

def wait_maze_and_walk(direction, gold0, s):
    # До появления лабиринта spawned-дрон стоит на своей точке.
    # measure() внутри maze возвращает позицию treasure,
    # а до maze здесь ожидаем None.
    while measure() == None:
        if num_items(Items.Gold) != gold0:
            return False

    return walk_left(direction, gold0, s)

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
    x = get_pos_x()

    while x < tx:
        move(East)
        x = x + 1

    while x > tx:
        move(West)
        x = x - 1

    y = get_pos_y()

    while y < ty:
        move(North)
        y = y + 1

    while y > ty:
        move(South)
        y = y - 1

def go_to_point(row, index_in_row, rows, count_in_row, s):
    y = ((2 * row + 1) * s) // (2 * rows)
    x = ((2 * index_in_row + 1) * s) // (2 * count_in_row)

    go_to(x, y)

def inside(direction, x, y, s):
    if direction == East:
        return x < s - 1

    if direction == West:
        return x > 0

    if direction == North:
        return y < s - 1

    if direction == South:
        return y > 0

    return False

def walk_left(direction, gold0, s):
    while num_items(Items.Gold) == gold0:
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True

        left = left_of(direction)
        right = right_of(direction)

        x = get_pos_x()
        y = get_pos_y()

        # Здесь intentionally НЕ делаем can_move() перед move().
        # move() сам дешево вернёт False, если упёрлись в стену,
        # а на успешном ходе не платим лишний tick за can_move().
        if inside(left, x, y, s) and move(left):
            direction = left
        elif inside(direction, x, y, s) and move(direction):
            pass
        elif inside(right, x, y, s) and move(right):
            direction = right
        else:
            back = back_of(direction)

            if inside(back, x, y, s) and move(back):
                direction = back
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
        wait_maze_and_walk,
        direction_for(placed + 1),
        gold0,
        s
    )

    # Если игра не дала spawned-дрона,
    # текущая точка становится мастерской.
    if drone == None:
        return total

    return placed + 1