from _movement import *

def spawn_maze() -> None:
    if get_entity_type() == Entities.Treasure:
        harvest()
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def cycle(p: tuple[int, int], do_left_cycle: bool) -> None:
    fly(p)
    change_hat(Hats.Top_Hat)
    direction = North

    if do_left_cycle:
        walk = fly_left
    else:
        walk = fly_right

    while True:
        if get_entity_type() == Entities.Treasure:
            spawn_maze()
        direction = walk(direction)

clear()
ws = get_world_size()

for i in range(max_drones() - 1):
    spawn_drone(cycle, (random() * ws, random() * ws), i % 2 == 0)

p = (ws // 2, ws // 2)
fly(p)
spawn_maze()
cycle(p, False)
