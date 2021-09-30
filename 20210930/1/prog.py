#print(sorted(eval(input()), key = lambda num: num**2 % 100))
arr = list(eval(input()))
for i in range(len(arr)):
    for j in range(1, len(arr) - i):
        if arr[j]**2 % 100 < arr[j - 1]**2 % 100:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
print(arr)