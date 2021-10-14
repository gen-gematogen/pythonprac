import fractions
import decimal
s, w, *coef = input().split(',')
s = fractions.Fraction(s)
w = fractions.Fraction(w)
a_coef = []
a_val = fractions.Fraction('0')
cur_val = fractions.Fraction('1')
for i in coef[int(coef[0]) + 1: 0: -1]:
    a_val += fractions.Fraction(i) * cur_val
    cur_val *= s
b_coef = []
b_val = fractions.Fraction('0')
cur_val = fractions.Fraction('1')
for j in coef[len(coef) - 1: int(coef[0]) + 2: -1]:
    b_val += fractions.Fraction(j) * cur_val
    cur_val *= s
if b_val == 0:
    print(False)
else:
    print(a_val / b_val == w)

