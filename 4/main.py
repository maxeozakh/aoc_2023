lines = []
file_path = './input.txt'
# file_path = './test.txt'
test_result = 30


def convert_to_int(char):
    return int(char)


def filter_empty(char):
    return char is not ''


with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]


result = 0
dict = {}
for i, line in enumerate(lines):
    dict[i+1] = 1

for line in lines:

    id = int(line.split(':')[0][5:])
    numbers = line.split(': ')[1].split(' | ')
    x = numbers[0].split(' ')
    y = numbers[1].split(' ')

    bonus_card_id = id + 1

    all_items = filter(filter_empty, x)
    all_items = map(convert_to_int, all_items)
    available_items = filter(filter_empty, y)
    available_items = map(convert_to_int, available_items)

    for available_item in available_items:
        if (available_item in all_items):
            dict[bonus_card_id] += 1 * dict[id]
            bonus_card_id += 1


for value in dict.values():
    result += value
assert test_result == result


# 1: 1 * 0

# 1: 1
# 2: 2
# 3: 2
# 4: 2
# 5: 1
# 6: 1
