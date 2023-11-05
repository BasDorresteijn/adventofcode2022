import os
import math

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')
file = open(filename, 'r')
total = 0

for line in file:
    line = line.replace('\n', '')
    line = line[::-1]
    sub_total = 0
    five_multiplier = 1
    for c in line:
        if c == '-':
            sub_total -= ( 1 * five_multiplier )
        elif c == '=':
            sub_total -= ( 2 * five_multiplier )
        else:
            sub_total += int(c) * five_multiplier
        five_multiplier *= 5
    total += sub_total

print('Decimal total:', total)
five_multiplier = 20
five_height = 5**five_multiplier
total_fived = ''

while five_height >= 1:
    floored = math.floor(total / five_height)
    if floored > 1:
        total_fived += str(floored)
        total -= floored * five_height
    else:
        total_fived += '0'
    five_height /= 5

print(total_fived)
print('Fix own input manually afterwards ;)')   