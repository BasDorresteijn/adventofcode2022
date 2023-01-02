import os
import math

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')
file = open(filename, 'r')

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


def calcStackHeight(rockCount):
    stack = [
        ['b', 'b', 'b', 'b', 'b', 'b', 'b']
    ]

    windCount = 0
    extraHeight = 0
    toFindMatch = []
    cycleCount = 0
    patternFound = False
    skipPatterningDone = False
    startPatternHeight = 0
    max = rockCount

    i = 0
    while i < max:
        if not patternFound:
            if i == 500:
                startPatternHeight = len(stack)
                toFindMatch = []
                for toCopyStackItem in stack[-10:]:
                    toFindMatch.append(toCopyStackItem[:])

            if i > 500:
                cycleCount += 1
                if stack[-10:] == toFindMatch:
                    patternFound = True

        if not skipPatterningDone and patternFound:
            cyclesToSkip = math.floor((max - i) / cycleCount)
            cycleHeight = len(stack) - startPatternHeight
            extraHeight = cyclesToSkip * cycleHeight
            i += cyclesToSkip * cycleCount
            skipPatterningDone = True

        toAddRockCopy = []
        toAddRock = rocks[i % 5]
        for toCopyRockRow in toAddRock:
            toAddRockCopy.append(toCopyRockRow[:])

        for _ in range(4):
            windDirection = wind[windCount % len(wind)]
            windCount += 1

            if windDirection == '<':
                canMove = True
                for r in toAddRockCopy:
                    if r[0] != '.':
                        canMove = False

                if canMove:
                    for r in toAddRockCopy:
                        r.reverse()
                        item = r.pop()
                        r.insert(0, item)
                        r.reverse()

            if windDirection == '>':
                canMove = True
                for r in toAddRockCopy:
                    if r[len(r) - 1] != '.':
                        canMove = False

                if canMove:
                    for r in toAddRockCopy:
                        item = r.pop()
                        r.insert(0, item)

        placed = False
        posDepth = len(stack)
        toAddRockCopy.reverse()
        while not placed:
            posDepth -= 1
            for qIdx, q in enumerate(toAddRockCopy):
                if posDepth + qIdx >= len(stack):
                    continue
                top = stack[posDepth + qIdx]
                for pos in range(len(q)):
                    if q[pos] != '.' and top[pos] != '.':
                        placed = True
                        break
            if placed:
                break

            windDirection = wind[windCount % len(wind)]
            windCount += 1

            newList = []
            for toCopyStackItem in toAddRockCopy:
                newList.append(toCopyStackItem[:])

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
                toAddRockCopy = newList

        posDepth += 1

        for u in toAddRockCopy:
            if posDepth < len(stack):
                for hIdx, h in enumerate(u):
                    if h != '.':
                        stack[posDepth][hIdx] = h
            else:
                stack.append(u)

            posDepth += 1

        i += 1

    return len(stack) - 1 + extraHeight


print('Answer 1:', calcStackHeight(2022))
print('Answer 2:', calcStackHeight(1_000_000_000_000))
