from __builtins__ import *

def fmt_item(e: Entity) -> string:
    return str(e)[6:]

def _pow10(x):
    r = 1
    for _ in range(x):
        r = r * 10
    return r


def _floor(x):
    return x // 1


def _digit_char(d):
    if d < 1:
        return "0"
    if d < 2:
        return "1"
    if d < 3:
        return "2"
    if d < 4:
        return "3"
    if d < 5:
        return "4"
    if d < 6:
        return "5"
    if d < 7:
        return "6"
    if d < 8:
        return "7"
    if d < 9:
        return "8"
    return "9"


def _uint_to_string(x):
    x = _floor(x)

    if x <= 0:
        return "0"

    result = ""

    while x > 0:
        digit = x % 10
        result = _digit_char(digit) + result
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

    # Нужно место под:
    # целую часть + "." + хотя бы 1 знак после точки
    decimals = budget - int_len - 1

    if decimals < 1:
        return _uint_to_string(_floor(value))

    # Обрезаем лишние нули справа, но оставляем хотя бы 1 знак:
    # 5.00 -> 5.0
    # 5.01 -> 5.01
    while decimals > 1:
        factor = _pow10(decimals)
        scaled = _floor(value * factor)

        if scaled % 10 != 0:
            break

        decimals = decimals - 1

    factor = _pow10(decimals)
    scaled = _floor(value * factor)

    int_part = scaled // factor
    frac_part = scaled % factor

    return _uint_to_string(int_part) + "." + _uint_to_string_padded(frac_part, decimals)


def fmt_number(n, limit=5):
    if limit < 3:
        return "INF"

    if n >= 1000000000000000000:
        return "INF"

    if n <= -1000000000000000000:
        return "INF"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    if n == 0:
        return "0.0"

    suffix = ""
    scale = 1

    if n >= 1000000000000000:
        suffix = "Q"
        scale = 1000000000000000
    elif n >= 1000000000000:
        suffix = "T"
        scale = 1000000000000
    elif n >= 1000000000:
        suffix = "B"
        scale = 1000000000
    elif n >= 1000000:
        suffix = "M"
        scale = 1000000
    elif n >= 1000:
        suffix = "K"
        scale = 1000

    budget = limit - len(sign) - len(suffix)

    if budget < 1:
        return "INF"

    value = n / scale
    body = _fmt_scaled(value, budget)

    result = sign + body + suffix

    if len(result) <= limit:
        return result

    return "INF"