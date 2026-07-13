from __builtins__ import *

def transpose(arr: list[list]) -> list[list]:
    if not arr or not arr[0]:
        return []

    result = []
    for i in range(len(arr[0])):
        row = []
        for j in range(len(arr)):
            append(row, arr[j][i])
        result.append(row)
    return result
