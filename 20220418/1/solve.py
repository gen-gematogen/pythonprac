def solveSquare(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (min(x1, x2), max(x1, x2))
    elif d == 0:
        x1 = -b / (2 * a)
        return (x1, x1)
    else:
        return None
