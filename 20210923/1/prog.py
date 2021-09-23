def classify(n):
    a = n % 50
    b = n % 25
    c = n % 8
    return "A {} B {} C {}".format('+' if not a else '-', '+' if a and not b else '-', '+' if not c else '-')
    '''result = ""
    if n % 25 == 0:
        if n % 2:
            result += "A - B + "
        else:
            result += "A + B - "
    else:
        result += "A - B - "

    if n % 8:
        result += "C -"
    else:
        result += "C +"

    return result'''

print(classify(eval(input())))
