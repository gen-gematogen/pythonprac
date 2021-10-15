from math import *

def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

W, H, A, B, F = input().split()
W = int(W)
H = int(H)
A = int(A)
B = int(B)

X = [scale(0, W, A, B, i) for i in range(W)]
Y = [eval(F) for x in X]
my, My = min(Y), max(Y)
matr = [[' ' for i in range(W)] for j in range(H)]
for i in range(len(Y)):
    y = Y[i]
    # also needo to rotate the graphic upside down
    matr[int(scale(my, My, 0, H - 1, y))][i] = '*'
for row in matr[::-1]:
    print(*row)