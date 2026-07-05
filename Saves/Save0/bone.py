from __builtins__ import *
import move

def cycle():
    change_hat(Hats.Dinosaur_Hat)
    while True:
        res = measure()
        if res == None:
            change_hat(Hats.Gray_Hat)
            break
        else:
            x, y = res
            move_succeed = move.snake(x, y)
            if not move_succeed:
                change_hat(Hats.Gray_Hat)
                break
