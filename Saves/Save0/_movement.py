from __builtins__ import *


#     0 1 2 3
#     _ _ _ _
# 0 | x x x x
# 1 | x x x x
# 2 | x x x x
# 3 | x x x x
#
def make_flight_plan(
        dest: tuple[int, int],
        orig: tuple[int, int] | None = None,
        ws: int | None = None
) -> list[Direction]:
    if orig == None:
        orig = (get_pos_x(), get_pos_y())
    if ws == None:
        ws = get_world_size()

    dx = (dest[0] - orig[0]) % ws
    dy = (dest[1] - orig[1]) % ws

    if abs(dx) > ws // 2:
        dx = (abs(dx) - ws) * ((dx > 0) - (dx < 0))

    if abs(dy) > ws // 2:
        dy = (abs(dy) - ws) * ((dy > 0) - (dy < 0))

    plan = []
    for _ in range(abs(dx)):
        if dx > 0:
            append(plan, East)
        else:
            append(plan, West)

    for _ in range(abs(dy)):
        if dy > 0:
            append(plan, North)
        else:
            append(plan, South)

    return plan


def make_brush_flight_plan(
        dest: tuple[int, int],
        orig: tuple[int, int] | None = None,
        ws: int | None = None
) -> list[Direction]:
    if orig == None:
        orig = (get_pos_x(), get_pos_y())
    if ws == None:
        ws = get_world_size()

    dx = (dest[0] - orig[0]) % ws
    dy = (dest[1] - orig[1]) % ws

    if abs(dx) > ws // 2:
        dx = (abs(dx) - ws) * ((dx > 0) - (dx < 0))

    if abs(dy) > ws // 2:
        dy = (abs(dy) - ws) * ((dy > 0) - (dy < 0))

    plan = []
    for _ in range(abs(dx)):
        if dx > 0:
            append(plan, East)
        else:
            append(plan, West)

    return plan

# return moves made
def fly(
        dest: tuple[int, int],
        orig: tuple[int, int] | None = None,
        ws: int | None = None
) -> int:
    if orig == None:
        orig = (get_pos_x(), get_pos_y())
    if ws == None:
        ws = get_world_size()

    plan = make_flight_plan(dest, orig, ws)
    for direction in plan:
        move(direction)

    return len(plan)


def fly_left(direction: Direction) -> Direction:
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


def fly_right(direction: Direction) -> Direction:
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


def left_of(d: Direction) -> Direction:
    if d == North:
        return West
    if d == West:
        return South
    if d == South:
        return East
    return North


def right_of(d: Direction) -> Direction:
    if d == North:
        return East
    if d == East:
        return South
    if d == South:
        return West
    return North


def back_of(d: Direction) -> Direction:
    if d == North:
        return South
    if d == South:
        return North
    if d == East:
        return West
    return East
