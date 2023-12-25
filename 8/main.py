# file_path = './input.txt'
file_path = './test.txt'
test_result = 142
r_a = []
r = 0

lines = []
with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]


for line in lines:
    print(line)
    print('===========')

assert test_result == r
