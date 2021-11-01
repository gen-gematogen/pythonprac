import itertools
import sys

def slide(seq, n):
    i = 0
    for it in itertools.tee(seq, len(seq)):
        yield from itertools.islice(it, i, i + n)
        i += 1

exec(sys.stdin.read())