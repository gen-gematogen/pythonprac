from __future__ import annotations
import sys
from typing import get_type_hints

class check(type):
    def __init__(self, name, parents, ns):
        def check_annotations(self):
            annotations = get_type_hints(self, globalns = globals(), localns = ns)
            for name in annotations:
                if not hasattr(self, name) or not issubclass(type(getattr(self, name)), annotations[name]):
                        return False
            return True
        setattr(self, 'check_annotations', check_annotations)

exec(sys.stdin.read())
