from enum import IntEnum
import os

class Direction(IntEnum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

box_height = 50
position_x = 0
position_y = 0
direction = Direction.RIGHT

class Box:
    def __init__(self, map: list[list[str]], x_offset: int = 0, y_offset: int = 0) -> None:
        self.top: Box
        self.right: Box
        self.down: Box
        self.left: Box
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.box_data = read_box(map, x_offset, y_offset)

    def move(self, amount: int):
        global position_x
        global position_y
        global direction

        if amount == 0:
            return self

        if direction == Direction.RIGHT:
            if position_x + 1 == box_height:
                if self.right.box_data[position_y][0] != '#':
                    position_x = 0
                    return self.right.move(amount - 1)
                else:
                    return self
            elif self.box_data[position_y][position_x + 1] != '#':
                position_x += 1
                return self.move(amount - 1)
            else:
                return self
            
            
        if direction == Direction.LEFT:
            if position_x == 0:
                if self.left.box_data[position_y][box_height - 1] != '#':
                    position_x = box_height - 1
                    return self.left.move(amount - 1)
                else:
                    return self
            elif self.box_data[position_y][position_x - 1] != '#':
                position_x -= 1
                return self.move(amount - 1)
            else:
                return self
        

        if direction == Direction.DOWN:
            if position_y + 1 == box_height:
                if self.down.box_data[0][position_x] != '#':
                    position_y = 0
                    return self.down.move(amount - 1)
                else:
                    return self
            elif self.box_data[position_y + 1][position_x] != '#':
                position_y += 1
                return self.move(amount - 1)
            else:
                return self
        

        if direction == Direction.UP:
            if position_y == 0:
                if self.top.box_data[box_height - 1][position_x] != '#':
                    position_y = box_height - 1
                    return self.top.move(amount - 1)
                else:
                    return self
            elif self.box_data[position_y - 1][position_x] != '#':
                position_y -= 1
                return self.move(amount - 1)
            else:
                return self
                     

        return self
    



def read_box(map: list[list[str]], start_x: int = 0, start_y: int = 0) -> list[list[str]]:
    box: list[list[str]] = []
    for i in range(box_height):
        box_row = []
        map_row = map[start_y + i]
        for j in range(box_height):
            box_row.append(map_row[start_x + j])
        box.append(box_row)

    return box


def print_box(box = list[list[str]]) -> None:
    for i in box:
        for j in i:
            print(j, end='')
        print()


def read_map() -> tuple[list[list[str]], str]:
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'file.txt')
    file = open(filename, 'r')
    instructions: str

    map: list[list[str]] = []
    for line in file:
        line = line.replace('\n', '')
        if line == '':
            instructions = file.readline()
            break

        row = []
        for i in line:
            row.append(i)
        map.append(row)

    return map, instructions


map, instructions = read_map()

box1 = Box(map, box_height)
box2 = Box(map, box_height * 2)
box3 = Box(map, box_height, box_height)
box4 = Box(map, y_offset=box_height*2)
box5 = Box(map, box_height, box_height*2)
box6 = Box(map, y_offset=box_height*3)

# mapping 
box1.top = box5
box1.right = box2
box1.left = box2
box1.down = box3

box2.top = box2
box2.right = box1
box2.left = box1
box2.down = box2

box3.top = box1
box3.right = box3
box3.left = box3
box3.down = box5

box4.top = box6
box4.right = box5
box4.left = box5
box4.down = box6

box5.top = box3
box5.right = box4
box5.left = box4
box5.down = box1

box6.top = box4
box6.right = box6
box6.left = box6
box6.down = box4

movement_cache = ''
box = box1
for i in instructions:
    if i == 'R' or i == 'L':
        if movement_cache != '':
            to_move_squares = int(movement_cache)
            box = box.move(to_move_squares)
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
box = box.move(to_move_squares)
print(position_x, position_y)

result = (position_y + box.y_offset + 1) * 1000 + (position_x + box.x_offset + 1) * 4 + direction 
print('Answer 1:', result)