from _movement import *


def walk_left(direction: Direction) -> Direction:
    left = left_of(direction)
    if move(left):
        return left

    if move(direction):
        return direction

    right = right_of(direction)
    if move(right):
        return right

    back = back_of(direction)
    move(back)
    return back


def walk_right(direction: Direction) -> Direction:
    right = right_of(direction)
    if move(right):
        return right

    if move(direction):
        return direction

    left = left_of(direction)
    if move(left):
        return left

    back = back_of(direction)
    move(back)
    return back


def spawn_maze() -> None:
    if get_entity_type() == Entities.Treasure:
        harvest()
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def cycle(p: tuple[int, int], left_wall: bool) -> None:
    fly(p)
    change_hat(Hats.Top_Hat)
    direction = North

    if left_wall:
        walk = walk_left
    else:
        walk = walk_right

    while True:
        if get_entity_type() == Entities.Treasure:
            spawn_maze()
        direction = walk(direction)


clear()
set_world_size(20)
ws = get_world_size()

for i in range(max_drones() - 1):
    spawn_drone(cycle, (random() * ws, random() * ws), i % 2 == 0)

p = (ws // 2, ws // 2)
fly(p)
spawn_maze()
cycle(p, False)
