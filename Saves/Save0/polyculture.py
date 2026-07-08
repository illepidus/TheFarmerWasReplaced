from __builtins__ import *
from helpers import fmt_item, fmt_number
from farming import smart_plant

clear()

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


def slave(flight_plan: list[Direction], target: Entity):
    for direction in flight_plan:
        move(direction)
    return smart_plant(target)


def master(x: int, y: int, target: Entity = Entities.Grass, debug_mode: bool = True) -> None:
    start_time = get_time()
    prev_time = start_time
    start_items = {}

    if debug_mode:
        for item in Items:
            # noinspection PyTypeChecker
            start_items[item] = num_items(item)

    change_hat(Hats.Brown_Hat)
    x0 = get_pos_x()
    y0 = get_pos_y()
    world_size = get_world_size()
    fly((x0, y0), (x, y), world_size)

    initial_plant = smart_plant(target)
    if initial_plant != target:
        quick_print("initial seeding failed: wanted" + str(target) + ", got " + str(initial_plant))
        return

    plant_map = {}

    while True:
        if debug_mode:
            time = get_time()
            if time - prev_time > 5:
                prev_time = time
                msg = {}
                for item in Items:
                    # noinspection PyTypeChecker
                    q1 = num_items(item)
                    q0 = start_items[item]
                    dt = time - start_time

                    if q0 != q1:
                        # noinspection PyTypeChecker
                        msg[fmt_item(item)] = fmt_number((q1 - q0) / dt * 60)

                quick_print(msg)

        companion = get_companion()
        if companion == None:
            quick_print("companion was not found for ", target)
            return

        map_key = str(companion[1][0]) + "_" + str(companion[1][1])
        if map_key not in plant_map or plant_map[map_key] != companion[0]:
            plan = make_flight_plan((x, y), companion[1], world_size)
            radius = 3
            if len(plan) <= radius:
                while True:
                    # noinspection PyTypeChecker
                    drone = spawn_drone(slave, plan, companion[0])
                    if drone != None:
                        break

                plant_map[map_key] = wait_for(drone)

        while True:
            if can_harvest():
                harvest()
                break
            else:
                if get_water() < .75:
                    use_item(Items.Water)
                else:
                    if target != Entities.Grass:
                        use_item(Items.Fertilizer)

        if target != Entities.Grass:
            plant(target)


y = 4
for j in range(5):
    if j % 2 == 0:
        x = 4
    else:
        x = 0

    for i in range(4):
        debug = False
        if i == 0 and j == 0:
            debug = True
        # noinspection PyTypeChecker
        spawn_drone(master, x, y, Entities.Grass, debug)
        x += 8
    y += 4
