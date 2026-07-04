from __builtins__ import *


def _noop():
    return


def _to(get_pos_f, dec_direction, inc_direction, target_pos):
    pos = get_pos_f()

    direction = dec_direction
    if abs(target_pos - pos) * 2 < get_world_size():
        if (target_pos - pos) > 0:
            direction = inc_direction
    else:
        if (target_pos - pos) < 0:
            direction = inc_direction

    while get_pos_f() != target_pos:
        move(direction)


def to(x, y):
    _to(get_pos_x, West, East, x)
    _to(get_pos_y, South, North, y)


def brush(f=_noop, x0=0, y0=0, x1=get_world_size(), y1=get_world_size()):
    if min(x0, y0, x1, y1) < 0:
        print("brush args error")
    for x in range(x0, x1):
        for y in range(y0, y1):
            to(x, y)
            f()
