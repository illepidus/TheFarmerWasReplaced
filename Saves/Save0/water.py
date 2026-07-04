from __builtins__ import *

def apply():
    while get_water() <= 0.75:
        if not use_item(Items.Water):
            break