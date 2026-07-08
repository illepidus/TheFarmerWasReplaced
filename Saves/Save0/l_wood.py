from polyculture import *

_ = Leaderboards.Wood

y = 3
for j in range(5):
    if j % 2 == 0:
        x = 3
    else:
        x = 6

    for i in range(4):
        # noinspection PyTypeChecker
        spawn_drone(cycle, x, y, Entities.Tree, (Items.Wood, 10000000000), False)
        x += 7
    y += 3
