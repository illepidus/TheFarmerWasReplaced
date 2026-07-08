from polyculture import *

y = 3
for j in range(5):
    if j % 2 == 0:
        x = 3
    else:
        x = 0

    for i in range(4):
        # noinspection PyTypeChecker
        spawn_drone(cycle, x, y, Entities.Grass, (Items.Hay, 2000000000))
        x += 7
    y += 3
