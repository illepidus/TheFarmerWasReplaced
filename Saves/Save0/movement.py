from __builtins__ import *


#     0 1 2 3
#     _ _ _ _
# 0 | x x x x
# 1 | x x x x
# 2 | x x x x
# 3 | x x x x
#
def make_flight_plan(p0: tuple[int, int], p1: tuple[int, int], ws: int) -> list[Direction]:
    dx = (p1[0] - p0[0]) % ws
    dy = (p1[1] - p0[1]) % ws

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
def fly(p0: tuple[int, int], p1: tuple[int, int], ws: int) -> int:
    plan = make_flight_plan(p0, p1, ws)
    for direction in plan:
        move(direction)
    return len(plan)
