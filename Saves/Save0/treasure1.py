from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    change_hat(Hats.Purple_Hat)

    gold0 = num_items(Items.Gold)

    # Мастер запускает только один dispatcher.
    # Дальше дерево само размножается и развозит детей.
    master_target = spawn_positioned_drones_tree(s, gold0)

    # Мастер едет не в угол поля, а в дальнюю точку сетки.
    go_to(master_target[0], master_target[1])

    # Лабиринт появляется здесь.
    plant(Entities.Bush)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    # Мастер тоже участвует из своей точки сетки.
    walk_left(North, gold0, s)

def spawn_positioned_drones_tree(s, gold0):
    total = total_drones_for_field(s)

    if total <= 1:
        return [0, 0]

    rows = ceil_sqrt(total)

    master_target = find_farthest_target(s, total, rows)
    master_x = master_target[0]
    master_y = master_target[1]

    child_count = total - 1

    if child_count <= 0:
        return master_target

    spawn_drone(
        spawn_tree,
        0,
        child_count,
        s,
        gold0,
        total,
        rows,
        master_x,
        master_y
    )

    return master_target

def spawn_tree(first_order, count, s, gold0, total, rows, master_x, master_y):
    # Этот дрон отвечает за диапазон child-задач:
    # first_order ... first_order + count - 1

    if count <= 0:
        return

    if count == 1:
        target = child_point_for_order(
            first_order,
            s,
            total,
            rows,
            master_x,
            master_y
        )

        return wait_maze_and_walk(
            target[0],
            target[1],
            direction_for(first_order + 1),
            gold0,
            s
        )

    left_count = count // 2
    right_count = count - left_count

    drone = spawn_drone(
        spawn_tree,
        first_order,
        left_count,
        s,
        gold0,
        total,
        rows,
        master_x,
        master_y
    )

    if drone == None:
        spawn_tree(
            first_order,
            left_count,
            s,
            gold0,
            total,
            rows,
            master_x,
            master_y
        )

    return spawn_tree(
        first_order + left_count,
        right_count,
        s,
        gold0,
        total,
        rows,
        master_x,
        master_y
    )

def wait_maze_and_walk(tx, ty, direction, gold0, s):
    # До появления лабиринта поле свободное.
    go_to(tx, ty)

    # Ждём создания лабиринта.
    # Внутри maze measure() возвращает позицию treasure.
    while measure() == None:
        if num_items(Items.Gold) != gold0:
            return False

    return walk_left(direction, gold0, s)

def total_drones_for_field(s):
    total = max_drones()

    if total > s * s:
        total = s * s

    return total

def find_farthest_target(s, total, rows):
    best_x = 0
    best_y = 0
    best_dist = -1

    row = 0

    while row < rows:
        count = points_in_row(row, rows, total)
        i = 0

        while i < count:
            x = point_x(i, count, s)
            y = point_y(row, rows, s)

            dist = x + y

            if dist > best_dist:
                best_dist = dist
                best_x = x
                best_y = y

            i = i + 1

        row = row + 1

    return [best_x, best_y]

def child_point_for_order(order, s, total, rows, master_x, master_y):
    # order = 0..child_count-1
    #
    # Возвращает order-ую НЕ-мастерскую точку сетки.
    # Идём примерно от дальних точек к ближним, чтобы дальние дети
    # стартовали раньше внутри дерева.

    seen = 0
    row = rows - 1

    while row >= 0:
        count = points_in_row(row, rows, total)
        i = count - 1

        while i >= 0:
            x = point_x(i, count, s)
            y = point_y(row, rows, s)

            if not (x == master_x and y == master_y):
                if seen == order:
                    return [x, y]

                seen = seen + 1

            i = i - 1

        row = row - 1

    return [0, 0]

def points_in_row(row, rows, total):
    return ((row + 1) * total) // rows - (row * total) // rows

def point_x(index_in_row, count_in_row, s):
    return ((2 * index_in_row + 1) * s) // (2 * count_in_row)

def point_y(row, rows, s):
    return ((2 * row + 1) * s) // (2 * rows)

def ceil_sqrt(n):
    r = 1

    while r * r < n:
        r = r + 1

    return r

def direction_for(i):
    r = i % 4

    if r == 0:
        return North
    if r == 1:
        return East
    if r == 2:
        return South

    return West

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