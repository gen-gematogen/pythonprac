def SUB(a, b):
    if str(type(a)) == "<class 'tuple'>" or str(type(a)) == "<class 'list'>":
        return type(a)([i for i in a if i not in b])
    return a - b
print(SUB(*eval(input())))

 