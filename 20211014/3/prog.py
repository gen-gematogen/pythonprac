s0 = input()
W = len(s0)
H  = 2
s = input()
gas = 0
liquid = 0
while  s != s0:
    gas += s.count('.')
    liquid += s.count('~')
    H += 1
    s = input()

liquid_rows = (liquid + H - 3) // (H - 2) # with ceil round
gas_rows = W - 2 - liquid_rows
print('#' * H)
print(('#' + '.' * (H - 2) + '#\n') * gas_rows, end = '')
print(('#' + '~' * (H - 2) + '#\n') * liquid_rows, end = '')
print('#' * H)
if liquid > gas:
    row_len = round(gas / liquid * 20)
    print('.' * row_len + ' ' + f"{gas:>{len(str(liquid)) + row_len}}" + '/' + str(gas + liquid))
    print('~' * 20 + ' ' + str(liquid) + '/' + str(gas + liquid))
else:
    row_len = round(liquid / gas * 20)
    print('.' * 20 + ' ' + str(gas) + '/' + str(gas + liquid))
    print('~' * row_len + ' ' + f'{liquid:>{len(str(gas)) + row_len}}' + '/' + str(gas + liquid))