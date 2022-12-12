import os
import time

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')

map = []
start_point = (0, 0)
end_point = (0, 0)

with open(filename, 'r') as file:
    for xIdx, i in enumerate(file):
        i = i.replace('\n', '')
        submap = []
        for yIdx, char in enumerate(i):
            if char == 'S':
                char = 'a'
                start_point = (xIdx, yIdx)
            if char == 'E':
                char = 'z'
                end_point = (xIdx, yIdx)
            submap.append(char)
        map.append(submap)

if len(map) == 0:
    exit()

max_width = len(map)
max_height = len(map[0])
points_checked = []
print_map = False


def find_points(start_points, path_count=0, print_map=print_map):
    if end_point in start_points:
        return path_count

    next_points = []
    for point in start_points:
        left_point = (point[0] - 1, point[1])
        if can_add_point(point, left_point, next_points):
            next_points.append(left_point)

        right_point = (point[0] + 1, point[1])
        if can_add_point(point, right_point, next_points):
            next_points.append(right_point)

        top_point = (point[0], point[1] + 1)
        if can_add_point(point, top_point, next_points):
            next_points.append(top_point)

        bottom_point = (point[0], point[1] - 1)
        if can_add_point(point, bottom_point, next_points):
            next_points.append(bottom_point)

    points_checked.extend(start_points)
    if print_map:
        print_map()
        time.sleep(0.2)
    return find_points(next_points, path_count + 1)


def can_add_point(current_point, next_point, next_points):
    if next_point in next_points:
        return False

    next_point_x = next_point[0]
    next_point_y = next_point[1]

    if next_point in points_checked:
        return False
    if next_point_x < 0 or next_point_x >= max_width:
        return False
    if next_point_y < 0 or next_point_y >= max_height:
        return False

    current_point_value = ord(map[current_point[0]][current_point[1]])
    next_point_value = ord(map[next_point[0]][next_point[1]])

    return current_point_value + 1 >= next_point_value


def print_map():
    print("")
    print("")
    print("")
    print("")
    for xIdx, i in enumerate(map):
        for yIdx, j in enumerate(map[xIdx]):
            if (xIdx, yIdx) == start_point:
                print('S', end="")
            elif (xIdx, yIdx) == end_point:
                print('E', end="")
            elif (xIdx, yIdx) in points_checked:
                print('-', end="")
            else:
                print(j, end="")
        print("")


print("Answer 1: ", find_points([start_point], 0))
