from _farming import *
from _movement import *

def _slave(flight_plan: list[Direction], target: Entity):
    for direction in flight_plan:
        move(direction)
    return smart_plant(target)


def _master(x: int, y: int, target: Entity = Entities.Grass) -> None:
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
                    drone = spawn_drone(_slave, plan, companion[0])
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

clear()
y = 3
for j in range(5):
    if j % 2 == 0:
        x = 3
    else:
        x = 0

    for i in range(4):
        # noinspection PyTypeChecker
        spawn_drone(_master, x, y, Entities.Grass)
        x += 7
    y += 3
