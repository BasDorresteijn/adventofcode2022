import os
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')

file = open(filename, 'r')

values = []
currentValue = 1
for line in file:
    line = line.replace('\n', '')
    if line == 'noop':
        values.append(currentValue)
    else:
        values.append(currentValue)
        values.append(currentValue)
        value = int(line.replace('addx ', ''))
        currentValue += value


def getSignalStrength(cycleCount):
    return values[cycleCount - 1] * cycleCount


def drawRow(cycleCountFrom):
    for i in range(40):
        icon = '.'
        if -2 < i - values[cycleCountFrom + i] < 2:
            icon = '#'
        print(icon, end='')
    print()


sum = 0
for i in range(6):
    sum += getSignalStrength(20 + i * 40)


print('Answer 1:', sum)

print('Answer 2: ')

for i in range(6):
    drawRow(i * 40)
