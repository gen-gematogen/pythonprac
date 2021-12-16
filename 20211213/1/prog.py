import random
import asyncio
import sys

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
    tasks, n = [], 0
    events = dict()

    for p in range(4):
        b = 2**(p+1)
        for i in range(0, len(L), b):
            events[(i, i + b)] = asyncio.Event()
            if b == 2:
                l_event = None
                r_event = None
            else:
                l_event = events[(i, i + b // 2)]
                r_event = events[(i + b // 2, i + b)]
            new_event = events[(i, i + b)]
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, r_event, l_event, new_event)))
        await asyncio.gather(*tasks)

L = list(eval(input()))
random.shuffle(L)
LL = L.copy()

asyncio.run(joiner())
print(L)
