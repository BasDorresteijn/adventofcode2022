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
        self.top: lambda amount: Box
        self.right: lambda amount: Box
        self.down: lambda amount: Box
        self.left: lambda amount: Box
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.box_data = read_box(map, x_offset, y_offset)

    def move(self, amount: int):
        global position_x
        global position_y
        global direction

        if amount == 0:
            return self
        
        self.box_data[position_y][position_x] = 'L'

        if direction == Direction.RIGHT:
            if position_x + 1 == box_height:
                return self.right(amount - 1)
            elif self.box_data[position_y][position_x + 1] != '#':
                position_x += 1
                return self.move(amount - 1)
            else:
                return self
            
            
        if direction == Direction.LEFT:
            if position_x == 0:
                return self.left(amount - 1)
            elif self.box_data[position_y][position_x - 1] != '#':
                position_x -= 1
                return self.move(amount - 1)
            else:
                return self
        

        if direction == Direction.DOWN:
            if position_y + 1 == box_height:
                return self.down(amount - 1)
            elif self.box_data[position_y + 1][position_x] != '#':
                position_y += 1
                return self.move(amount - 1)
            else:
                return self
        

        if direction == Direction.UP:
            if position_y == 0:
                return self.top(amount - 1)
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


def print_box(box: Box) -> None:
    for i in box.box_data:
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


def change_box(self_box: Box, new_box: Box, new_pos_x: int, new_pos_y: int, new_direction: Direction) -> Box:
    global position_x
    global position_y
    global direction

    if new_box.box_data[new_pos_y][new_pos_x] != '#':
        position_x = new_pos_x
        position_y = new_pos_y
        direction = new_direction
        return new_box
    
    return self_box

def default_right(self_box: Box, new_box: Box, amount: int) -> Box:
    global position_x

    if new_box.box_data[position_y][0] != '#':
        position_x = 0
        return new_box.move(amount)
    
    return self_box


def default_left(self_box: Box, new_box: Box, amount: int) -> Box:
    global position_x

    if new_box.box_data[position_y][box_height - 1] != '#':
        position_x = box_height - 1
        return new_box.move(amount)
    
    return self_box

def default_top(self_box: Box, new_box: Box, amount: int) -> Box:
    global position_y

    if new_box.box_data[box_height - 1][position_x] != '#':
        position_y = box_height - 1
        return new_box.move(amount)
    
    return self_box
    
def default_down(self_box: Box, new_box: Box, amount: int) -> Box:
    global position_y

    if new_box.box_data[0][position_x] != '#':
        position_y = 0
        return new_box.move(amount)
    
    return self_box

# mapping 
box1.top = lambda amount: default_top(box1, box5, amount)
box1.right = lambda amount: default_right(box1, box2, amount)
box1.left = lambda amount: default_left(box1, box2, amount)
box1.down = lambda amount: default_down(box1, box3, amount)

box2.top = lambda amount: default_top(box2, box2, amount)
box2.right = lambda amount: default_right(box2, box1, amount)
box2.left = lambda amount: default_left(box2, box1, amount)
box2.down = lambda amount: default_down(box2, box2, amount)

box3.top = lambda amount: default_top(box3, box1, amount)
box3.right = lambda amount: default_right(box3, box3, amount)
box3.left =lambda amount: default_left(box3, box3, amount)
box3.down = lambda amount: default_down(box3, box5, amount)

box4.top = lambda amount: default_top(box4, box6, amount)
box4.right =lambda amount: default_right(box4, box5, amount)
box4.left = lambda amount: default_left(box4, box5, amount)
box4.down = lambda amount: default_down(box4, box6, amount)

box5.top = lambda amount:  default_top(box5, box3, amount)
box5.right =lambda amount:  default_right(box5, box4, amount)
box5.left =lambda amount:  default_left(box5, box4, amount)
box5.down = lambda amount:  default_down(box5, box1, amount)

box6.top = lambda amount:  default_top(box6, box4, amount)
box6.right = lambda amount:  default_right(box6, box6, amount)
box6.left = lambda amount:  default_left(box6, box6, amount)
box6.down = lambda amount:  default_down(box6, box4, amount)

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

result = (position_y + box.y_offset + 1) * 1000 + (position_x + box.x_offset + 1) * 4 + direction 
print('Answer 1:', result)



# Part 2:

position_x = 0
position_y = 0
direction = Direction.RIGHT

def change_box(self_box: Box, new_box: Box, new_pos_x: int, new_pos_y: int, new_direction: Direction, amount: int) -> Box:
    global position_x
    global position_y
    global direction

    if new_box.box_data[new_pos_y][new_pos_x] != '#':
        position_x = new_pos_x
        position_y = new_pos_y
        direction = new_direction
        return new_box.move(amount)
    
    return self_box

# mapping 

box1.top = lambda amount: change_box(box1, box6, 0, position_x, Direction.RIGHT, amount)
box1.right = lambda amount: default_right(box1, box2, amount)
box1.left = lambda amount: change_box(box1, box4, 0, box_height - 1 - position_y, Direction.RIGHT, amount) 
box1.down = lambda amount: default_down(box1, box3, amount)

box2.top = lambda amount: default_top(box2, box6, amount)
box2.right = lambda amount: change_box(box2, box5, box_height - 1, box_height - 1 - position_y, Direction.LEFT, amount)
box2.left = lambda amount: default_left(box2, box1, amount)
box2.down = lambda amount: change_box(box2, box3, box_height - 1, position_x, Direction.LEFT, amount)

box3.top = lambda amount: default_top(box3, box1, amount)
box3.right = lambda amount: change_box(box3, box2, position_y, box_height - 1, Direction.UP, amount)
box3.left =lambda amount: change_box(box3, box4, position_y, 0, Direction.DOWN, amount)
box3.down = lambda amount: default_down(box3, box5, amount)

box4.top = lambda amount: change_box(box4, box3, 0, position_x, Direction.RIGHT, amount)
box4.right = lambda amount: default_right(box4, box5, amount)
box4.left = lambda amount: change_box(box4, box1, 0, box_height - 1 - position_y, Direction.RIGHT, amount) 
box4.down = lambda amount: default_down(box4, box6, amount)

box5.top = lambda amount:  default_top(box5, box3, amount)
box5.right =lambda amount:  change_box(box5, box2, box_height - 1, box_height - 1 - position_y, Direction.LEFT, amount)
box5.left =lambda amount:  default_left(box5, box4, amount) 
box5.down = lambda amount:  change_box(box5, box6, box_height - 1, position_x, Direction.LEFT, amount)

box6.top = lambda amount:  default_top(box6, box4, amount)
box6.right = lambda amount:  change_box(box6, box5, position_y, box_height - 1, Direction.UP, amount) 
box6.left = lambda amount:  change_box(box6, box1, position_y, 0, Direction.DOWN, amount)
box6.down = lambda amount:  default_down(box6, box2, amount)

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

result = (position_y + box.y_offset + 1) * 1000 + (position_x + box.x_offset + 1) * 4 + direction 
print('Answer 2:', result)
