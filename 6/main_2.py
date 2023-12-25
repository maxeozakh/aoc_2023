lines = []
file_path = './input.txt'
# file_path = './test.txt'
test_result = 71503
r = 1
r_arr = []

with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]

data = []
t = [x for x in lines[0].split(':')[1].replace(' ', '') if x.isdigit()]
d = [x for x in lines[1].split(':')[1].replace(' ', '') if x.isdigit()]

t = int(''.join(t))
d = int(''.join(d))
dict = {t: d}

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
