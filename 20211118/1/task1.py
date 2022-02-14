from functools import wraps
def objcount(cls):
    class wrap_cls(cls):
        counter = 0
        def __init__(self):
            super().__init__()
            wrap_cls.counter += 1
        def __del__(self):
            try:
                super().__del__()
            except:
                pass
            wrap_cls.counter -= 1
    return wrap_cls

import sys
exec(sys.stdin.read())
