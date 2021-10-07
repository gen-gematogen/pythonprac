def Pareto(*data):
    ans = []
    for i in data:
        for j in data:
            if i[0] <= j[0] and i[1] <= j[1] and (i[0] < j[0] or i[1] < j[1]):
                break
        else:
            ans.append(i)
    return tuple(ans)
print(Pareto(*eval(input())))