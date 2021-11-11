class InvalidInput(ValueError):
    pass
class BadTriangle(ValueError):
    pass

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except:
        raise InvalidInput
    else:
        try:
            area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
        except:
            raise BadTriangle
        if area == 0:
            raise BadTriangle
        else:
            return area

while True:
    try:
        area = triangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print('Not a triangle')
    else:
        print('%.2f'%area)
        break
