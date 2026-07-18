from _movement import *


def spawn_maze(size: int) -> None:
    harvest()
    plant(Entities.Bush)
    substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def collect_and_keep_maze(size: int) -> tuple[int, int]:
    substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
    return measure()


def scout():
    d0 = fly_left(North)
    x0 = get_pos_x()
    y0 = get_pos_y()

    d = d0
    sequence = []
    while True:
        d = fly_left(d)
        sequence.append((d, back_of(d)))
        if get_pos_x() == x0 and get_pos_y() == y0 and d == d0:
            break

    return sequence


def cycle(i: int, j: int, maze_size: int, target_gold: int | None = None, flips: int = 0):
    fly((i * maze_size + maze_size // 2, j * maze_size + maze_size // 2))

    for _ in range(flips):
        do_a_flip()

    while True:
        done = False
        fly((i * maze_size + maze_size // 2, j * maze_size + maze_size // 2))
        spawn_maze(maze_size)
        sequence = scout()
        found = 0

        while not done:
            for entry in sequence:
                if get_entity_type() == Entities.Treasure:
                    if found < 300:
                        collect_and_keep_maze(maze_size)
                        found += 1
                    else:
                        found = 0
                        done = True
                        harvest()
                    if target_gold != None and num_items(Items.Gold) >= target_gold:
                        return
                move(entry[0])
