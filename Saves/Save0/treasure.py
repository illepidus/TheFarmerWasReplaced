from __builtins__ import *

def cycle(s=get_world_size()):
    clear()
    change_hat(Hats.Purple_Hat)

    gold0 = num_items(Items.Gold)

    # plan = [master_x, master_y, ready_tick]
    # Дети уже заспавнены и едут к своим точкам.
    plan = spawn_positioned_drones(s, gold0)

    # Мастер едет в свою, ближнюю, точку раскладки.
    go_to(plan[0], plan[1])

    # Ждём, пока дальние дети точно доедут.
    wait_until_tick(plan[2], gold0)

    # Лабиринт появляется здесь.
    plant(Entities.Bush)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    # Мастер тоже участвует из своей точки.
    walk_left(North, gold0, s)

def wait_maze_and_walk(tx, ty, direction, gold0, s):
    # Spawned-дрон сам едет к своей точке.
    # До появления лабиринта поле свободное.
    go_to(tx, ty)

    # Стоим на месте до появления maze.
    # В maze measure() возвращает позицию treasure.
    while measure() == None:
        pass

    return walk_left(direction, gold0, s)

def wait_until_tick(target_tick, gold0):
    while get_tick_count() < target_tick:
        # Дешёвое действие на 1 tick.
        # Заодно безопасный выход, если gold уже изменился.
        if num_items(Items.Gold) != gold0:
            return

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

def point_x(index_in_row, count_in_row, s):
    return ((2 * index_in_row + 1) * s) // (2 * count_in_row)

def point_y(row, rows, s):
    return ((2 * row + 1) * s) // (2 * rows)

def point_id(x, y, s):
    return x * s + y

def contains(items, value):
    for item in items:
        if item == value:
            return True

    return False

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

        # Не делаем can_move() перед move():
        # успешный move и так дорогой, а неуспешный move дешёвый.
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

def total_drones_for_field(s):
    total = max_drones()

    if total > s * s:
        total = s * s

    return total

def find_nearest_target(s, total, rows):
    best_x = 0
    best_y = 0
    best_dist = 999999

    row = 0

    while row < rows:
        count = points_in_row(row, rows, total)
        i = 0

        while i < count:
            x = point_x(i, count, s)
            y = point_y(row, rows, s)
            dist = x + y

            if dist < best_dist:
                best_dist = dist
                best_x = x
                best_y = y

            i = i + 1

        row = row + 1

    return [best_x, best_y]

def spawn_positioned_drones(s, gold0):
    start_tick = get_tick_count()

    total = total_drones_for_field(s)

    if total <= 1:
        return [0, 0, start_tick]

    rows = ceil_sqrt(total)

    # Мастер берёт ближайшую точку из той же равномерной раскладки.
    master_target = find_nearest_target(s, total, rows)
    master_x = master_target[0]
    master_y = master_target[1]

    child_count = total - 1
    spawned = 0
    spawned_ids = []

    # Абсолютный tick, когда все дети должны быть на местах.
    ready_tick = start_tick

    # Дальние точки отдаём детям первыми:
    # каждый следующий spawn задержан на 200 ticks,
    # поэтому дальним детям нужна фора.
    while spawned < child_count:
        best_x = 0
        best_y = 0
        best_id = -1
        best_dist = -1

        row = 0

        while row < rows:
            count = points_in_row(row, rows, total)
            i = 0

            while i < count:
                x = point_x(i, count, s)
                y = point_y(row, rows, s)
                pid = point_id(x, y, s)

                if not (x == master_x and y == master_y) and not contains(spawned_ids, pid):
                    dist = x + y

                    if dist > best_dist:
                        best_dist = dist
                        best_x = x
                        best_y = y
                        best_id = pid

                i = i + 1

            row = row + 1

        if best_id == -1:
            return [master_x, master_y, ready_tick]

        spawned_ids.append(best_id)

        drone = spawn_drone(
            wait_maze_and_walk,
            best_x,
            best_y,
            direction_for(spawned + 1),
            gold0,
            s
        )

        if drone == None:
            return [master_x, master_y, ready_tick]

        # Оценка:
        # spawned+1 успешных spawn_drone по 200 ticks,
        # потом ребёнок едет best_dist шагов по 200 ticks.
        #
        # +10 — маленький запас на get_pos_x/get_pos_y/measure.
        child_ready_tick = start_tick + (spawned + 1 + best_dist) * 200 + 10

        if child_ready_tick > ready_tick:
            ready_tick = child_ready_tick

        spawned = spawned + 1

    return [master_x, master_y, ready_tick]