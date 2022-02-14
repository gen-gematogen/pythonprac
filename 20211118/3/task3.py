class Alpha:
    __slots__ = [chr(i) for i in range(ord('a'), ord('z') + 1)]

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
