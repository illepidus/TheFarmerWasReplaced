from __builtins__ import *


def cycle(size=get_world_size()):
    clear()
    set_world_size(size)
    half_size = size // 2 - 1

    for _ in range(half_size):
        move(North)

    change_hat(Hats.Dinosaur_Hat)

    while True:
        i = 0

        for _ in range(size):
            for _ in range(half_size):
                i += move(South)

            i += move(East)

            for _ in range(half_size):
                i += move(North)

            i += move(East)

        for _ in range(size):
            for _ in range(half_size):
                i += move(North)

            i += move(West)

            for _ in range(half_size):
                i += move(South)

            i += move(West)

        if i < size ** 2:
            change_hat(Hats.Gray_Hat)
            return