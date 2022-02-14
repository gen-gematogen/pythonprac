class Num:
    def __get__(self, obj, cls):
        return getattr(self, 'value', 0)
    def __set__(self, obj, val = 0):
        try:
            self.value = val.real
        except:
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
