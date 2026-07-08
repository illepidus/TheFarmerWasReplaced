from _farming import *
from _movement import *
from _util import *


def _plant_row(
        length: int,
        p0_target: tuple[int, int] | None = None,
        p0_drone: tuple[int, int] | None = None,
        world_size: int | None = None
) -> tuple[list[int], tuple[int, int]] | None:
    if length < 1:
        quick_print("negative plant row length")
        return None

    if p0_drone == None:
        p0_drone = (get_pos_x(), get_pos_y())

    if world_size == None:
        world_size = get_world_size()

    if p0_target == None:
        p0_target = p0_drone

    fly(p0_drone, p0_target, world_size)
    sizes = []

    for i in range(length):
        if smart_plant(Entities.Cactus) != Entities.Cactus:
            quick_print("was not able to plant cactus")
            return None
        append(sizes, measure())
        if i != length - 1:
            move(East)

    return sizes, (p0_target[0] + length - 1, p0_target[1])


def _sort_line(
        data: list[int],
        p0_target: tuple[int, int],
        p0_drone: tuple[int, int],
        world_size: int,
        is_row: bool,
) -> tuple[list[int], tuple[int, int]] | None:
    length = len(data)
    left = 0
    right = length - 1
    i = right
    direction = -1

    x0 = p0_target[0]
    y0 = p0_target[1]
    x = p0_drone[0]
    y = p0_drone[1]

    if is_row:
        swap_direction = West
    else:
        swap_direction = South

    while left < right:
        while left < i <= right:
            if data[i] < data[i - 1]:
                if is_row:
                    target_x = x0 + i
                    target_y = y0
                else:
                    target_x = x0
                    target_y = y0 + i

                fly((x, y), (target_x, target_y), world_size)
                x = target_x
                y = target_y

                tmp = data[i]
                data[i] = data[i - 1]
                data[i - 1] = tmp

                swap(swap_direction)

            i = i + direction

        if direction < 0:
            left += 1
            direction = 1
            i = left + 1
        else:
            right -= 1
            direction = -1
            i = right

    return data, (x, y)


def _sort_row(
        data: list[int],
        p0_target: tuple[int, int],
        p0_drone: tuple[int, int],
        world_size: int,
) -> tuple[list[int], tuple[int, int]] | None:
    return _sort_line(data, p0_target, p0_drone, world_size, True)


def _sort_column(
        data: list[int],
        p0_target: tuple[int, int],
        p0_drone: tuple[int, int],
        world_size: int,
) -> tuple[list[int], tuple[int, int]] | None:
    return _sort_line(data, p0_target, p0_drone, world_size, False)


def _plant_and_sort_row(
        length: int,
        p0_target: tuple[int, int] | None = None,
        p0_drone: tuple[int, int] | None = None,
        world_size: int | None = None
) -> tuple[list[int], tuple[int, int]] | None:
    plant_result = _plant_row(length, p0_target, p0_drone, world_size)
    if plant_result == None:
        return None
    row, (x, y) = plant_result
    return _sort_row(row, p0_target, (x, y), world_size)


def cycle(x, y, w, h):
    change_hat(Hats.Cactus_Hat)
    world_size = get_world_size()
    drone_p = get_pos_x(), get_pos_y()

    drones = []
    for i in range(h - 1):
        # noinspection PyTypeChecker
        append(drones, spawn_drone(_plant_and_sort_row, w, (x, y + i), drone_p, world_size))

    last_row_result = _plant_and_sort_row(w, (x, y + h - 1), drone_p, world_size)
    if last_row_result == None:
        quick_print("master plant_and_sort_row failed")
        return

    rows = []
    for drone in drones:
        r = wait_for(drone)
        if r == None:
            quick_print("slave plant_and_sort_row failed")
            return
        append(rows, wait_for(drone)[0])
    append(rows, last_row_result[0])

    columns = transpose(rows)
    drone_p = last_row_result[1]

    for i in range(h - 1):
        # noinspection PyTypeChecker
        append(drones, spawn_drone(_sort_column, columns[i], (x + i, y), drone_p, world_size))

    last_column_result = _sort_column(columns[h - 1], (x + w - 1, x), drone_p, world_size)
    if last_column_result == None:
        quick_print("master sort_column failed")
        return

    for drone in drones:
        r = wait_for(drone)
        if r == None:
            quick_print("slave sort_column failed")
            return

    harvest()


while True:
    cycle(0, 0, 32, 32)
