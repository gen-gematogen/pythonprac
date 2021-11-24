class Alpha:
    __slots__ = [chr(i) for i in range(ord('a'), ord('z') + 1)]

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

