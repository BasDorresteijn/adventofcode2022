import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')
file = open(filename, 'r')


stack = [
    ['b', 'b', 'b', 'b', 'b', 'b', 'b']
]

wind = list(file.readline())

rocks = [
    [
        ['.', '.', 'x', 'x', 'x', 'x', '.']
    ],
    [
        ['.', '.', '.', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', 'x', '.', '.'],
        ['.', '.', '.', 'x', '.', '.', '.']
    ],
    [
        ['.', '.', '.', '.', 'x', '.', '.'],
        ['.', '.', '.', '.', 'x', '.', '.'],
        ['.', '.', 'x', 'x', 'x', '.', '.']
    ],
    [
        ['.', '.', 'x', '.', '.', '.', '.'],
        ['.', '.', 'x', '.', '.', '.', '.'],
        ['.', '.', 'x', '.', '.', '.', '.'],
        ['.', '.', 'x', '.', '.', '.', '.']
    ],
    [
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.']
    ]
]

windCount = 0
windListLength = len(wind)

for i in range(2022):
    toAddRock = []
    toAddRockReal = rocks[i % 5]
    for i in toAddRockReal:
        toAddRock.append(i[:])

    for _ in range(4):
        windDirection = wind[windCount % windListLength]
        windCount += 1

        if windDirection == '<':
            canMove = True
            for r in toAddRock:
                if r[0] != '.':
                    canMove = False

            if canMove:
                for r in toAddRock:
                    r.reverse()
                    item = r.pop()
                    r.insert(0, item)
                    r.reverse()

        if windDirection == '>':
            canMove = True
            for r in toAddRock:
                if r[len(r) - 1] != '.':
                    canMove = False

            if canMove:
                for r in toAddRock:
                    item = r.pop()
                    r.insert(0, item)

    placed = False
    posDepth = len(stack)
    toAddRock.reverse()
    while not placed:
        posDepth -= 1
        for qIdx, q in enumerate(toAddRock):
            if posDepth + qIdx >= len(stack):
                continue
            top = stack[posDepth + qIdx]
            for pos in range(len(q)):
                if q[pos] != '.' and top[pos] != '.':
                    placed = True
                    break
        if placed:
            break

        windDirection = wind[windCount % windListLength]
        windCount += 1

        newList = []
        for x in toAddRock:
            newList.append(x[:])

        if windDirection == '<':
            canMove = True
            for r in newList:
                if r[0] != '.':
                    canMove = False

            if not canMove:
                continue

            for r in newList:
                r.reverse()
                item = r.pop()
                r.insert(0, item)
                r.reverse()

        if windDirection == '>':
            canMove = True
            for r in newList:
                if r[len(r) - 1] != '.':
                    canMove = False

            if not canMove:
                continue

            for r in newList:
                item = r.pop()
                r.insert(0, item)

        for zIdx, z in enumerate(newList):
            if posDepth + zIdx >= len(stack):
                continue
            top = stack[posDepth + zIdx]
            for pos in range(len(z)):
                if z[pos] != '.' and top[pos] != '.':
                    canMove = False
                    break

        if canMove:
            toAddRock = newList

    posDepth += 1

    for u in toAddRock:
        if posDepth < len(stack):
            for hIdx, h in enumerate(u):
                if h != '.':
                    stack[posDepth][hIdx] = h
        else:
            stack.append(u)

        posDepth += 1

# DEBUG PRINT TREE
# for i in stack:
    # print(i)


print('Answer 1:', len(stack) - 1)

# 5238 TO HIGH
