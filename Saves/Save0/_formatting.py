from __builtins__ import *

def fmt_item(e: Entity) -> string:
    return str(e)[6:]


def _floor(x):
    return x // 1


def _uint_to_string(x):
    x = _floor(x)

    if x <= 0:
        return "0"

    result = ""

    while x > 0:
        digit = x % 10
        result = str(digit) + result
        x = x // 10

    return result


def _uint_to_string_padded(x, width):
    result = _uint_to_string(x)

    while len(result) < width:
        result = "0" + result

    return result


def _int_len_0_999(value):
    if value >= 100:
        return 3

    if value >= 10:
        return 2

    return 1


def _fmt_scaled(value, budget):
    int_len = _int_len_0_999(value)
    decimals = budget - int_len - 1

    if decimals < 1:
        return _uint_to_string(_floor(value))

    while decimals > 1:
        factor = 10 ** decimals
        scaled = _floor(value * factor)

        if scaled % 10 != 0:
            break

        decimals = decimals - 1

    factor = 10 ** decimals
    scaled = _floor(value * factor)

    int_part = scaled // factor
    frac_part = scaled % factor

    return _uint_to_string(int_part) + "." + _uint_to_string_padded(frac_part, decimals)


def fmt_number(n, limit=5):
    if limit < 3:
        return "INF"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    if n == 0:
        return "0.0"

    suffix = ""
    scale = 1

    if n >= 10 ** 15:
        suffix = "Q"
        scale = 10 ** 15
    elif n >= 10 ** 12:
        suffix = "T"
        scale = 10 ** 12
    elif n >= 10 ** 9:
        suffix = "B"
        scale = 10 ** 9
    elif n >= 10 ** 6:
        suffix = "M"
        scale = 10 ** 6
    elif n >= 10 ** 3:
        suffix = "K"
        scale = 10 ** 3

    budget = limit - len(sign) - len(suffix)

    if budget < 1:
        return "INF"

    value = n / scale
    body = _fmt_scaled(value, budget)

    result = sign + body + suffix

    if len(result) <= limit:
        return result

    return "INF"
