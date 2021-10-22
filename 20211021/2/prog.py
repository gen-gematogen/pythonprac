from math import *

s = input().split(' ')
functions = dict()
lines_count = 1

while s[0] != 'quit':
    if s[0][0] == ':':
        # it's a function
        functions[s[0][1:]] = (s[1:-1], s[-1])
    else:
        ev = dict()
        for i in range(len(s[1:])):
            ev[functions[s[0]][0][i]] = eval(s[i + 1])
        print(eval(functions[s[0]][1], None, ev))
    s = input().split(' ')
    lines_count += 1
print(eval(s[1] + '.format(' + str(len(functions) + 1) + ',' + str(lines_count) + ')'))