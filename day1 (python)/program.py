import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')

file = open(filename, 'r')

tempTotal = 0
totals = []

for i in file:
    if i == '\n':
        totals.append(tempTotal)
        tempTotal = 0
    else:
        tempTotal += int(i)

totals.sort(reverse=True)

print('answer 1:', totals[0])

print('answer 2:', totals[0] + totals[1] + totals[2])
