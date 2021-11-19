from functools import wraps
def iint(typ):
    def decor(fn):
        def new_f(*args):
            for arg in args:
                if type(arg) is not typ:
                    raise TypeError
            return fn(*args)
        return new_f
    return decor
#@iint(str)
#def fun(a, b):
#    return a*2+b
#print(fun('1', '1'))    
#print(fun(1, 2))
def dumpc(cls):
    class newcl(cls):
        def __str__(self):
            res = super().__str__()
            return  f">>{res}"
    return newcl
@dumpc
class A(str):
    pass
print(A("fdafa"))
