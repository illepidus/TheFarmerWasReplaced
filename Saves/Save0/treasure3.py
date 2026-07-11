from _movement import *

def cycle(p: tuple[int, int], substance) -> None:
    fly(p)
    while True:
        if get_entity_type() == Entities.Treasure:
            use_item(Items.Weird_Substance, substance)


clear()
ws = 5
set_world_size(ws)
substance = ws * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

for i in range(ws):
    for j in range(ws):
        spawn_drone(cycle, (j, i), substance)

fly((0, 0), (2, 2), ws)
while True:
    harvest()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)
    t0 = get_tick_count()
    while True:
        t = get_tick_count()
        if t > t0 + 62500:
            break
