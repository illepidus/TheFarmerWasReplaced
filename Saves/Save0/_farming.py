from __builtins__ import *

def smart_plant(target: Entity) -> Entity | None:
    entity = get_entity_type()

    if entity == target:
        return target

    if entity != None:
        harvest()

    ground = get_ground_type()

    if target == Entities.Grass:
        if ground == Grounds.Soil:
            till()
        return target
    else:
        if ground == Grounds.Grassland:
            till()
        if plant(target):
            return target
        else:
            return get_entity_type()