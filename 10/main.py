
'''

# algo

1. find all legit ways from the position of the X (firstly, X will be the beast itself).
2. loop through all the results from the step 1 and recursevely do it until there is no more roads to explore
3. lists of the already processed roads should be maintained


# questions

1. how to keep track of the depth?


'''


file_path = './input.txt'
# file_path = './test.txt'
test_result = 142
r_a = []
r = 0

lines = []


with open(file_path) as f:
    lines = [list(line.rstrip('\n')) for line in f]


def get_starting_position(lines):
    for i_l, line in enumerate(lines):
        for i_s, s in enumerate(line):
            if s == 'S':
                return [i_l, i_s]

    return None


assert get_starting_position([
    ['.', '.'],
    ['.', 'S']
]) == [1, 1]
assert get_starting_position([
    ['S', '.'],
    ['.', '']
]) == [0, 0]
assert get_starting_position([
    ['.', '.'],
    ['.', '.']
]) == None


def get_label(lines, point):
    [y, x] = point
    return lines[y][x]


def get_relative_to_point(obj, subj):
    [y1, x1] = obj
    [y2, x2] = subj

    if (x2 < x1):
        return 4
    if (x2 > x1):
        return 6
    if (y2 < y1):
        return 8
    if (y2 > y1):
        return 2


assert get_relative_to_point([0, 0], [1, 0]) == 2
assert get_relative_to_point([1, 0], [0, 0]) == 8
assert get_relative_to_point([0, 0], [0, 1]) == 6
assert get_relative_to_point([0, 1], [0, 0]) == 4

directions_by_label = {
    '-': [4, 6],
    '|': [2, 8],
    'F': [6, 2],
    'L': [6, 8],
    '7': [4, 2],
    'J': [4, 8],
    'S': [2, 4, 6, 8]
}


def is_possible_to_reach(point_from, point_to):
    relativity = get_relative_to_point(point_from, point_to)
    label = get_label(lines, point_from)
    directions_from = directions_by_label[label]
    label_to = get_label(lines, point_to)

    if (label == 'S'):
        if relativity == 2:
            return label_to in ['|', 'L', 'J']
        if relativity == 8:
            return label_to in ['|', 'F', '7']
        if relativity == 4:
            return label_to in ['-', 'J', '7']
        if relativity == 6:
            return label_to in ['-', 'L', '7']
    else:
        return relativity in directions_from


def get_paths(lines, point, point_from=None):
    # print('lets find legit paths for point', point)
    [y, x] = point
    point_label = get_label(lines, point)

    if point_label == '.':
        # print('its a dot!', '\n')
        return []

    points_around = [
        [y - 1, x],
        [y + 1, x],
        [y, x - 1],
        [y, x + 1],
    ]

    if (point_from in points_around):
        points_around.remove(point_from)

    # print(points_around)
    # filter to prevent checks out of the boundaries
    points_around = [neighbor_point for neighbor_point in points_around if
                     neighbor_point[0] >= 0 and
                     neighbor_point[1] >= 0 and
                     neighbor_point[0] < len(lines) and
                     neighbor_point[1] < len(lines[0]) and
                     get_label(lines, [neighbor_point[0], neighbor_point[1]]) != '.']
    # print(f"points around are {points_around}")

    result = []
    for neighbor in points_around:
        is_possible = is_possible_to_reach(point, neighbor)
        print(
            f'from {get_label(lines, point)} to {get_label(lines, neighbor)}? {is_possible}')
        if (is_possible):
            result.append(neighbor)

    # print('result is', result, '\n')
    return result


starting_position = get_starting_position(lines)
# test_lines = [['.', '.', 'F', '7', '.'],
#               ['.', 'F', 'J', '|', '.'],
#               ['S', 'J', '.', 'L', '7'],
#               ['|', 'F', '-', '-', 'J'],
#               ['L', 'J', '.', '.', '.']]
# assert get_paths(test_lines, starting_position) == [[3, 0], [2, 1]]
# assert get_paths(test_lines, [3, 0]) == [[2, 0], [4, 0]]
# assert get_paths(test_lines, [3, 0], [2, 0]) == [[4, 0]]
# assert get_paths(test_lines, [4, 0]) == [[3, 0], [4, 1]]
# assert get_paths(test_lines, [2, 4]) == [[3, 4], [2, 3]]
# assert get_paths(test_lines, [0, 3], [0, 2]) == [[1, 3]]
# assert get_paths(test_lines, [0, 0]) == []

finished = False
counter = 1
paths = []
prev_step = starting_position
next_step = get_paths(lines, starting_position)[0]
paths.append(next_step)
print(next_step, get_label(lines, next_step))
while not finished:
    # print(prev_step, next_step)
    temp = next_step
    next_step = get_paths(lines, next_step, prev_step)[0]
    prev_step = temp
    label = get_label(lines, next_step)
    paths.append(next_step)
    print(next_step, label)
    counter += 1
    if (label == 'S'):
        finished = True

r = counter // 2
print(r)
