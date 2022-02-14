class Num:
    def __get__(self, obj, cls):
        return getattr(obj, 'value', 0)
    def __set__(self, obj, val = 0):
        try:
            self.value = val.real
        except:
<<<<<<< HEAD
            self.value = val.__len__()

class C:
        num = Num()

print(C().num)
c, d = C(), C()
c.num = d.num = 2
print(c.num+d.num)
c.num = "qwerqwerqwer"
print(c.num+d.num)
d.num = range(10, 1000, 7)
print(c.num+d.num)
=======
            value = val.__len__()
        obj.value = value

import sys
exec(sys.stdin.read())
>>>>>>> 1b2541c4017363f2cef4a376482b9c712b6a7afa
