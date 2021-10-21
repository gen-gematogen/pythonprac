from math import *

s = input().split(' ')
functions = dict()

while s[0] != 'quit':
    if s[0][0] == ':':
        # it's a function
        functions[s[0][1:]] = (s[1], s[2])
    else:
        ev = dict()
        ev[functions[s[0]][0]] = eval(s[1])
        print(eval(functions[s[0]][1], None, ev))
    s = input().split(' ')
print(len(functions) + 1)