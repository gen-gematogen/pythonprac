import sys

data = sys.stdin.buffer.read()
n = data[0]
l = len(data) - 1
k = data[0:1]
data = data[1:]
slices = []

for i in range(n):
    slices.append(data[i * l // n: (i + 1) * l // n])

slices.sort()

#sys.stdout.buffer.write(k)
for i in slices:
    #sys.stdout.buffer.write(i)
    k += i
sys.stdout.buffer.write(k)
