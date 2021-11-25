import sys

data = sys.stdin.buffer.readline()
n = data[0]
#data = data[1:]
l = len(data) - 1
k = n
print(l)
slices = []
L = 1
while L < l:
    sz = (l - L) // k
    slices.append(data[L:L+sz])
    k -= 1
    L += sz
    #L = i*l//k + 1
    #R = (i+1)*l//k + 1
    #slices.append(data[L: R])
    #k -= 1
    #l -= len(slices[-1])
    #print(L, R, R - L)

slices.sort()

k = 0
for i in slices:
    print(i, k)
    k += 1

sys.stdout.buffer.write(data[:1])
for i in slices:
    sys.stdout.buffer.write(i)
