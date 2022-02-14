class Alpha:
    __slots__ = [chr(i) for i in range(ord('a'), ord('z') + 1)]

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        arr = []
        for i in range(ord('a'), ord('z') + 1):
            val = getattr(self, chr(i), None)
            if val:
                arr.append(f'{chr(i)}: {val}')
        return ', '.join(arr)

class AlphaQ:
     Ж

alp = Alpha(c=10, z=2, a=42)
alp.e = 123
print(alp)
=======
    def __init__(self, **f):
        for field in f:
            setattr(self, field, f[field])
    def __str__(self):
        res = []
        for f in self.__slots__:
            if hasattr(self, f):
                res.append(f'{f}: {getattr(self, f)}')
        return ', '.join(res)

class AlphaQ:
    fields = {}
   
    def __setattr__(self, letter, val):
        self.fields[letter] = val

    def __getattr__(self, letter):
        try:
            return self.fields[letter]
        except:
            raise AttributeError

    def __init__(self, **f):
        self.fields.update(f)

    def __str__(self):
        res = []
        for f in sorted(self.fields):
            res.append(f'{f}: {self.fields[f]}')
        return ', '.join(res)

import sys
exec(sys.stdin.read())

>>>>>>> 1b2541c4017363f2cef4a376482b9c712b6a7afa
