def sign(val):
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def linear_interpolation(val, x0, y0, x1, y1):
    return y0 + ((val - x0) * (y1 - y0))/(x1 - x0)