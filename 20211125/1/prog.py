import sys

data = sys.stdin.buffer.readline()
n = data[0]
l = len(data) - 1
k = n
slices = []
L = 1
while L < l:
    sz = (l - L) // k
    slices.append(data[L:L+sz])
    k -= 1
    L += sz

slices.sort()

sys.stdout.buffer.write(data[:1])
for i in slices:
    sys.stdout.buffer.write(i)
