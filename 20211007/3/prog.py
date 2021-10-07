def Bisect(val, arr):
    if len(arr) > 1:
        m = len(arr) // 2
        if arr[m] > val:
            return Bisect(val, arr[:m])
        else:
            return Bisect(val, arr[m:])
    return arr[0] == val
print(Bisect(*eval(input())))