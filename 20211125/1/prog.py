import sys

data = sys.stdin.buffer.read()
n = data[0]
l = len(data) - 1
k = n
slices = []

#L = 1
#while L < l:
#    sz = (l - L) // k
#    slices.append(data[L:L+sz])
#    k -= 1
#    L += sz

for i in range(n):
    slices.append(data[1 + i * l // n: 1 + (i + 1) // n])

slices.sort()

sys.stdout.buffer.write(data[:1])
for i in slices:
    sys.stdout.buffer.write(i)
