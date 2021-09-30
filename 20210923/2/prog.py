def solve():
    summ = 0
    n = eval(input())
    while n > 0:
        summ += n
        if summ > 21:
            print(summ)
            break
        n = eval(input())
    else:
        print(n)

solve()
