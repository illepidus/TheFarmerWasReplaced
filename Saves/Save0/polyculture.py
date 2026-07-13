from _farming import *
from _movement import *


def _plant_companion(flight_plan: list[Direction], target: Entity):
    for direction in flight_plan:
        move(direction)
    return smart_plant(target)


def cycle(x: int, y: int, target: Entity, until: tuple[Item, int] | None = None, single_mode=False) -> None:
    x0 = get_pos_x()
    y0 = get_pos_y()
    world_size = get_world_size()
    fly((x, y), (x0, y0), world_size)

    initial_plant = smart_plant(target)
    if initial_plant != target:
        quick_print("initial seeding failed: wanted" + str(target) + ", got " + str(initial_plant))
        return

    plant_map = {}

    while True:
        if until != None:
            current = num_items(until[0])
            if current >= until[1]:
                break

        companion = get_companion()
        if companion == None:
            quick_print(
                "companion was not found for", target,
                "standing on", get_ground_type(),
                "with", get_entity_type(), "planed")
            return

        map_key = str(companion[1][0]) + "_" + str(companion[1][1])
        if map_key not in plant_map or plant_map[map_key] != companion[0]:
            plan = make_flight_plan(companion[1], (x, y), world_size)

            if single_mode:
                plant_map[map_key] = _plant_companion(plan, companion[0])
                fly((x, y), companion[1], world_size)
            else:
                while True:
                    # noinspection PyTypeChecker
                    drone = spawn_drone(_plant_companion, plan, companion[0])
                    if drone != None:
                        plant_map[map_key] = wait_for(drone)
                        break

        while True:
            if can_harvest():
                harvest()
                break
            else:
                if get_water() < .75:
                    use_item(Items.Water)
                else:
                    use_item(Items.Fertilizer)

        if target != Entities.Grass:
            plant(target)
