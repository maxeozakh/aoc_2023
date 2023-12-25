lines = []
file_path = './input.txt'
# file_path = './test.txt'
test_result = 281

with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]

nums_as_string = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]
mapa = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
arr = []

for i, line in enumerate(lines):
    temp_arr = []
    for ns in nums_as_string:
        y = [{i: mapa[ns]} for i in range(len(line)) if line.startswith(ns, i)]
        if (len(y)):
            for z, element in enumerate(y):
                temp_arr.append(y[z])
    for j, char in enumerate(line):
        if (char.isdigit()):
            obj = {j: int(char)}
            temp_arr.append(obj)

    temp_arr.sort()
    arr.append(temp_arr)

result = 0
for j, line in enumerate(arr):
    buffer = str(line[0].values()[0]) + str(line[len(line) - 1].values()[0])
    buffer_res = int(buffer)
    result += buffer_res

assert test_result == result
