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
