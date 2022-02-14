print([i for i in range(*(eval(input()))) if i != 1 and all([i % j for j in range(2, int(i**0.5) + 1)])])
