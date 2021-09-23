n = eval(input())
a = b = n

while a < n + 3:
    while b < n + 3:
        ans = "{}*{}=".format(a, b)
        c = a * b
        
        summ = 0
        tmp = c
        while tmp:
            summ += tmp%10
            tmp //= 10

        if summ == 6:
            ans += ":=)"
        else:
            ans += str(c)
        print(ans, end = ' ')
        b += 1
    b = n
    a += 1
    print()
