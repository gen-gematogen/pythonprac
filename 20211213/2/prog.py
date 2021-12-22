import random
import asyncio
import math
from collections import defaultdict

L = eval(input())
random.shuffle(L)
LL = L.copy()

async def merge(b0, b1, e1, l_event, r_event, new_event):
    if b1 - b0 != 1:
        await l_event.wait()
        await r_event.wait()

    b, e0, i = b0, b1, b0
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0)
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    
    new_event.set()

async def joiner():
    tasks = []
    events = defaultdict(asyncio.Event)

    for p in range(math.ceil(math.log2(len(L)))):
        b = 2**(p+1)
        for i in range(0, len(L), b):
            if i + b // 2 >= len(L):
                events[(i, len(L))].set()
                continue
            l_event = events[(i, i + b // 2)]
            r_event = events[(i + b // 2, min(i + b, len(L)))]
            if b == 2:
                l_event.set()
                r_event.set()
            new_event = events[(i, min(i + b, len(L)))]
            tasks.append(asyncio.create_task(merge(i, i + b // 2, min(i + b, len(L)), r_event, l_event, new_event)))
        await asyncio.gather(*tasks)

asyncio.run(joiner())
print(L)
