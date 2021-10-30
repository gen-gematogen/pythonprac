import itertools
import sys

def slide(seq, n):
    i = 0
    while True:
        yield from itertools.islice(seq, i, i + n)
        i += 1

exec(sys.stdin.read())