from __builtins__ import *

def cycle(s=get_world_size(), budget=2**num_unlocked(Unlocks.Megafarm)):
    clear()
    plant(Entities.Bush)
    change_hat(Hats.Purple_Hat)

    gold0 = num_items(Items.Gold)

    substance = s * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    spawned_cells = []

    walk_branching_left(North, gold0, budget - 1, spawned_cells, s)

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

def plan_for(direction):
    return [
        left_of(direction),
        direction,
        right_of(direction),
    ]

def cell_id(s):
    return get_pos_x() * s + get_pos_y()

def contains(items, value):
    for item in items:
        if item == value:
            return True

    return False

def spawn_left_branch(first_direction, gold0, s):
    def worker(
            direction0=first_direction,
            gold_before=gold0,
            world_size=s
    ):
        if num_items(Items.Gold) != gold_before:
            return

        # Первый шаг принудительный:
        # ребёнок уходит именно в ветку, которую родитель не выбрал.
        if not move(direction0):
            return

        if get_entity_type() == Entities.Treasure:
            harvest()
            return

        # Дети никого не рожают.
        walk_branching_left(direction0, gold_before, 0, [], world_size)

    spawn_drone(worker)

def walk_branching_left(direction, gold0, children_left, spawned_cells, s):
    while num_items(Items.Gold) == gold0:
        if get_entity_type() == Entities.Treasure:
            harvest()
            return True

        open_dirs = []

        for d in plan_for(direction):
            if can_move(d):
                open_dirs.append(d)

        if len(open_dirs) == 0:
            direction = back_of(direction)
            move(direction)
        else:
            main_direction = open_dirs[0]

            # Спавним детей только если:
            # - есть альтернативные проходы;
            # - остался лимит детей;
            # - в этой клетке ещё не спавнили.
            if len(open_dirs) > 1 and children_left > 0:
                cell = cell_id(s)

                if not contains(spawned_cells, cell):
                    spawned_cells.append(cell)

                    i = 1
                    while i < len(open_dirs) and children_left > 0:
                        spawn_left_branch(open_dirs[i], gold0, s)
                        children_left = children_left - 1
                        i = i + 1

            move(main_direction)
            direction = main_direction

    return False