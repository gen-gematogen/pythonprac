def solveSquare(a, b, c):
    if a == 0:
        if b == 0:
            return None
        return -c / b
    
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

class SquareIO:
    def inputCoeff(self, name):
        return input(f"Input {name}:")

    def printResult(self, result):
        print(f"Solution: {result}")

def solve():
    a = int(SquareIO.inputCoeff('a'))
    b = int(SquareIO.inputCoeff('b'))
    c = int(SquareIO.inputCoeff('c'))

    SquareIO.printResult(solveSquare(a, b, c))
