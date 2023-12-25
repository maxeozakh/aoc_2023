import time
file_path = './input.txt'
# file_path = './test.txt'
test_result = 2
r_a = []
r = 0

lines = []
with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]


for line in lines:
    numbers = [int(x) for x in line.split(' ')]

    sequence_in = [numbers]
    diffs = []

    # part 1

    # to_check = sequence_in[len(sequence_in) - 1]
    # print(sequence_in)
    # while not all(x == to_check[0] for x in to_check):
    #     for i, n in enumerate(to_check):
    #         if i == len(to_check) - 1:
    #             break

    #         # print(abs(n - to_check[i + 1]))
    #         diffs.append(to_check[i + 1] - n)

    #     sequence_in.append(diffs)
    #     to_check = sequence_in[len(sequence_in) - 1]
    #     print('diffs', diffs, to_check)
    #     diffs = []

    to_check = sequence_in[len(sequence_in) - 1]
    while not all(x == to_check[0] for x in to_check):
        for i, n in enumerate(to_check):
            if i == len(to_check) - 1:
                break

            diffs.append(to_check[i + 1] - n)

        sequence_in.append(diffs)
        to_check = sequence_in[len(sequence_in) - 1]
        diffs = []

    temp = 0
    sequence_in.reverse()
    for x in sequence_in:
        temp = x[0] - temp

    r += temp

assert test_result == r
