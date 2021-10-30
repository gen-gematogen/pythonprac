import itertools
print(*list(filter(lambda x: x.count("TOR") == 2, list(''.join(i) for i in itertools.product(['O', 'R', 'T'], repeat = int(input()))))))