class Num:
    def __get__(self, obj, cls):
        return getattr(self, 'value', 0)
    def __set__(self, obj, val = 0):
        try:
            value = val.real
        except:
            value = val.__len__()
        self.value = value

class C:
    d = Num()

c = C()
p = C()
c.d = [1, 2]
print(c.d) #2
print(p.d) #2
p.d = 100
print(p.d) #100
print(c.d) #100
