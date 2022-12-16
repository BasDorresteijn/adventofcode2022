import os
import re


class Item:
    def __init__(self, next_options, rate):
        self.rate = rate
        self.next_options = next_options

    def __str__(self):
        return f"{self.next_options}({self.rate})"


class Result:
    def __init__(self, path, rate):
        self.path = path
        self.rate = rate


def find_shortest_path(start_points, end_point, path_count=0, passed_points=[]):
    if end_point in start_points:
        return path_count

    passed_points.extend(start_points)
    next_points = []
    for i in start_points:
        for j in map[i].next_options:
            if j not in passed_points and j not in next_points:
                next_points.append(j)

    if (path_count > max_steps):
        return max_steps + 1

    return find_shortest_path(next_points, end_point, path_count + 1, passed_points)


here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'file.txt')
file = open(filename, 'r')

map = {}
max_steps = 26


for i in file:
    i = i.replace('Valve ', '')
    valveName = i[0:2]
    i = i.replace(valveName + ' has flow rate=', '')
    rate = int(re.findall(r'\d+', i)[0])
    i = i.replace(str(rate), '')
    i = i.replace('; tunnels lead to valves ', '')
    i = i.replace('; tunnel leads to valve ', '')
    next_options = re.findall(r'[^,\s]+', i)
    map[valveName] = Item(next_options=next_options, rate=rate)

has_rate = []

for i in map:
    if map[i].rate > 0:
        has_rate.append(i)

has_rate.append('AA')

path_map = {}

for i in has_rate:
    path_map[i] = {}
    for j in has_rate:
        if i == j:
            continue

        if j in path_map and i in path_map[j]:
            path_map[i][j] = path_map[j][i]
            continue

        path_map[i][j] = find_shortest_path(
            [i], j, 0, []) + 1  # Always open valve!

all_possible_paths = {}


def check_stuff(current_point, time_count=0, rate=0, passed_points=[]):
    global highest_value
    passed_points.append(current_point)
    passed_points.sort()
    key = ''
    for i in passed_points:
        key += i

    if (key not in all_possible_paths) or (all_possible_paths[key].rate < rate):
        all_possible_paths[key] = Result(passed_points[1:], rate)

    if (time_count >= max_steps) or (len(passed_points) == len(path_map)):
        return

    rate = rate + ((max_steps - time_count) * map[current_point].rate)

    for i in path_map[current_point]:
        if i not in passed_points:
            check_stuff(i, time_count +
                        path_map[current_point][i], rate, passed_points[:])


check_stuff('AA', 0, 0, [])
items = list(all_possible_paths.items())
items.sort(key=lambda x: x[1].rate, reverse=True)

highest_value = 0

for idx, i in enumerate(items):
    for j in items:
        combinedList = i[1].path + j[1].path
        if len(combinedList) == len(set(combinedList)):
            if i[1].rate + j[1].rate > highest_value:
                print(i[0], j[0])
                highest_value = i[1].rate + j[1].rate

    if idx % 100 == 0:
        print(idx, 'of', len(items))

print("Answer 2", highest_value)
