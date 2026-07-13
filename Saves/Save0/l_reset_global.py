from __builtins__ import *
_T0_ = get_time()

def infinite_loop():
    def _f():
        return

    while True:
        _f()

def throw_exception(text: string):
    quick_print("exception:", text)
    _ = 0 / 0


def unlock_or_throw(u):
    if unlock(u):
        lvl = num_unlocked(u)
        cost = get_cost(u, lvl - 1)
        quick_print(get_time() - _T0_, "Unlocked", u, "lvl", lvl, "for", cost)
    else:
        throw_exception("Was not able to unlock " + str(u))

