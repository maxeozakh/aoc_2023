lines = []
# file_path = './input.txt'
file_path = './test.txt'
test_result = 467835
result = 0

with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]


def generate_dict():
    dict = []
    for row_index, line in enumerate(lines):
        is_processing = False
        l_len = 0
        str = ''
        str_index = None

        for char_index, char in enumerate(line):
            # start processing
            if (char.isdigit() and not is_processing):
                is_processing = True
                l_len += 1
                str += char
                str_index = char_index

            # processing ends
            elif (not char.isdigit() and is_processing):
                dict.append([int(str), row_index, str_index, l_len])

                is_processing = False
                str_index = None
                str = ''
                l_len = 0

            # stop processing in the end of the line
            elif (char_index == (len(line) - 1) and is_processing):
                l_len += 1
                str += char

                dict.append([int(str), row_index, str_index, l_len])

                is_processing = False
                str_index = None
                str = ''
                l_len = 0

            # processing in progress
            elif (char.isdigit() and is_processing):
                l_len += 1
                str += char

    return dict


def is_symbol(char):
    return not char.isdigit() and not char == '.'


assert is_symbol('.') == False
assert is_symbol('4') == False
assert is_symbol('#') == True


def is_connected_to_symbol(d):
    result = [False, None]
    [value, row, index, length] = d

    index_left = index - 1
    index_right = index + length

    row_top = row - 1
    row_bottom = row + 1
    lets_break = False
    for r in range(row_top, row_bottom + 1):
        if (lets_break):
            break
        if (r < 0):
            continue

        for i in range(index_left, index_right + 1):
            if (i < 0 or i > (len(lines[0]) - 1) or r > (len(lines) - 1)):
                continue
            if (is_symbol(lines[r][i])):
                result = [True, [lines[r][i], r, i]]
                lets_break = True
                break

    return result


dict = generate_dict()


for element in dict:
    [is_connected, data] = is_connected_to_symbol(element)
    if (is_connected and data[0] == '*'):
        [symbol, s_row, s_index] = data
    elif (is_connected):
        result += int(element[0])


# 1. we should extract dict from line, which will contain {x: [i, j, z]}
#    where is x = number, i is row, j is index and z is length
# 2. then we need a function that will check is number connected
# 3. and last function add things to sum

assert test_result == result
