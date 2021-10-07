from math import *

def Calc(s, t, u):
    def foo(x):
        x_ = eval(s)
        y = eval(t)
        x = x_
        return eval(u)
    return foo
fun = Calc(*eval(input()))
print(fun(eval(input())))
