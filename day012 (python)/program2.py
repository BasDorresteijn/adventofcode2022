import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')

map = []
start_point = (0, 0)
end_point = (0, 0)
all_start_points = []

with open(filename, 'r') as file:
    for xIdx, i in enumerate(file):
        i = i.replace('\n', '')
        submap = []
        for yIdx, char in enumerate(i):
            if char == 'S':
                char = 'a'
            if char == 'E':
                char = 'z'
                end_point = (xIdx, yIdx)
            if char == 'a':
                all_start_points.append((xIdx, yIdx))
            submap.append(char)
        map.append(submap)

if len(map) == 0:
    exit()

max_width = len(map)
max_height = len(map[0])
points_checked = []


def find_points(start_points, path_count=0):
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


lowest_result = 1412412904124
for xIdx, i in enumerate(all_start_points):
    print(xIdx, 'of', len(all_start_points))
    try:
        result = find_points([i], 0)
    except:
        continue
    finally:
        points_checked = []
    print(i, lowest_result)
    if result < lowest_result:
        lowest_result = result

print("Answer 2: ", lowest_result)
