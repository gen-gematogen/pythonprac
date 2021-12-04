from functools import wraps

class dump(type):
    def __init__(self, name, parents, ns):
        for method_name in ns:
            method = ns[method_name]
            if callable(method):
                @wraps(method)
                def new_method(*args, method = method, method_name = method_name, **kwargs):
                    print(f'{method_name}: {args[1:]}, {kwargs}')
                    return method(*args, **kwargs)
                setattr(self, method_name, new_method)
        return super().__init__(name, parents, ns)

import sys
exec(sys.stdin.read())
