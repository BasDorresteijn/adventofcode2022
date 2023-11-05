import os
from enum import IntEnum


class Direction(IntEnum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


def get_last_index(array: list[str], to_find_value: str):
    return len(array) - 1 - array[::-1].index(to_find_value)


def move_on_map(squares: int):
    global map
    global pos_x
    global pos_y
    global direction

    if direction == Direction.RIGHT:
        for _ in range(squares):
            next_pos_y = pos_y + 1
            if next_pos_y >= len(map[pos_x]) or map[pos_x][next_pos_y] == ' ':
                next_pos_y = min(map[pos_x].index('.'), map[pos_x].index('#'))

            if map[pos_x][next_pos_y] == '#':
                break
            pos_y = next_pos_y

    elif direction == Direction.LEFT:
        for _ in range(squares):
            next_pos_y = pos_y - 1
            if next_pos_y < 0 or map[pos_x][next_pos_y] == ' ':
                next_pos_y = max(
                    get_last_index(map[pos_x], '.'),
                    get_last_index(map[pos_x], '#')
                )

            if map[pos_x][next_pos_y] == '#':
                break

            pos_y = next_pos_y

    elif direction == Direction.UP:
        for _ in range(squares):
            next_pos_x = pos_x - 1
            if next_pos_x < 0 or pos_y >= len(map[next_pos_x]) or map[next_pos_x][pos_y] == ' ':
                next_pos_x = len(map)
                next_tile = ' '
                while next_tile == ' ':
                    next_pos_x -= 1
                    try:
                        next_tile = map[next_pos_x][pos_y]
                    except:
                        next_tile = ' '

            if map[next_pos_x][pos_y] == '#':
                break

            pos_x = next_pos_x

    elif direction == Direction.DOWN:
        for _ in range(squares):
            next_pos_x = pos_x + 1
            if next_pos_x >= len(map) or pos_y >= len(map[next_pos_x]) or map[next_pos_x][pos_y] == ' ':
                next_pos_x = -1
                next_tile = ' '
                while next_tile == ' ':
                    next_pos_x += 1
                    try:
                        next_tile = map[next_pos_x][pos_y]
                    except:
                        next_tile = ' '

            if map[next_pos_x][pos_y] == '#':
                break

            pos_x = next_pos_x


here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')
file = open(filename, 'r')
map: list[list[str]] = []
instructions: str

for line in file:
    line = line.replace('\n', '')
    if line == '':
        instructions = file.readline()
        break

    row = []
    for i in line:
        row.append(i)
    map.append(row)

pos_x = 0
pos_y = map[pos_x].index('.')
direction: Direction = Direction.RIGHT

movement_cache = ''
for i in instructions:
    if i == 'R' or i == 'L':
        if movement_cache != '':
            to_move_squares = int(movement_cache)
            move_on_map(to_move_squares)
            movement_cache = ''

        if i == 'R':
            if direction == Direction.UP:
                direction = Direction.RIGHT
            else:
                direction = direction + 1
        else:
            if direction == Direction.RIGHT:
                direction = Direction.UP
            else:
                direction = direction - 1
    else:
        movement_cache += i
to_move_squares = int(movement_cache)
move_on_map(to_move_squares)


print('Answer 1:', (pos_x + 1) * 1000 + (pos_y + 1) * 4 + direction)
