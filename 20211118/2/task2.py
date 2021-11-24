class Num:
    def __get__(self, obj, cls):
        return getattr(obj, 'value', 0)
    def __set__(self, obj, val = 0):
        try:
            value = val.real
        except:
            value = val.__len__()
        obj.value = value

import sys
exec(sys.stdin.read())
