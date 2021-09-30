matr1 = []
row = list(eval(input()))
n = len(row)
for i in range(n):
    matr1.append(row)
    row = list(eval(input()))
matr2 = []
for i in range(n - 1):
    matr2.append(row)
    row = list(eval(input()))
matr2.append(row)

ans = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += matr1[i][k] * matr2[k][j]

for i in ans:
    print(i)