from __builtins__ import *


# noinspection PyTypeChecker
def measure(action):
    before = {}
    for item in Items:
        before[item] = num_items(item)

    t0 = get_time()
    action()
    t1 = get_time()

    result = {'time': t1 - t0}
    for item in Items:
        diff = num_items(item) - before[item]
        if diff:
            result[item] = diff

    return result
