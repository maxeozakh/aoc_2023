lines = []
file_path = './input.txt'
# file_path = './test.txt'
test_result = 288
r = 1
r_arr = []

with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]

data = []
t = [int(x) for x in lines[0].split(':')[1].split(' ') if x.isdigit()]
d = [int(x) for x in lines[1].split(':')[1].split(' ') if x.isdigit()]

dict = {}
for i, ti in enumerate(t):
    dict[ti] = d[i]

for t in dict.keys():
    record = dict[t]
    counter = 0
    for i in range(0, t):
        speed = i * 1
        time_left = t - i

        if (speed * time_left > record):
            counter += 1

    r *= counter

assert test_result == r
