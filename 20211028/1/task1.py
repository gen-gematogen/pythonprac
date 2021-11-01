def fib(m, n):
    cur_fib, prev_fib = 1, 1

    if not m:
        yield 1
    
    for i in range(1, n + 1):
        if i >= m:
            yield cur_fib
        tmp = cur_fib
        cur_fib = cur_fib + prev_fib
        prev_fib = tmp
import sys
exec(sys.stdin.read())