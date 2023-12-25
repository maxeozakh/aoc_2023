# i can't solve part 2 >:|
import random
lines = []
file_path = './input.txt'
# file_path = './test.txt'
test_result = 46
result = 0

with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]


seeds_i = lines[0].split('seeds: ')[1].split(' ')
seeds = [int(i) for i in seeds_i]

# seeds_buffer = []
# for i, seed in enumerate(seeds):
#     if (i % 2 == 0):
#         for ii, j in enumerate(range(0, int(seeds[i + 1]))):
#             seeds_buffer.append(int(seed) + ii)

# seeds = seeds_buffer
# print(seeds_buffer)

# xxxx = []
# for s_i, seed in enumerate(seeds):
#     if (s_i % 2 == 0):
#         seed_int = int(seed)
#         xxxx.append(seed)

# print(min(xxxx))
# time.sleep(1232)

maps_separators = [i for i, x in enumerate(lines) if x == ""]
maps_separators.append(len(lines))

maps = []
for i, s in enumerate(maps_separators):
    buffer = []
    if (s + 2 > len(lines)):
        continue
    for x in range(s + 2, maps_separators[i + 1]):
        map_line = [int(m) for m in lines[x].split(' ')]

        buffer.append(map_line)
    maps.append(buffer)

maps.reverse()

done = False
# for i in range(1228100, 28582244, 4400):
# for i in range(1, 100, 1):
# 378910000
cycles = 0
while (done is False):
    cycles += 1
    ran_int = random.randint(1000, 28582244)
    # ran_int = random.randint(1, 100)

    # 378900950 prev attempt
    # 3669570
    for i in range(4360699, 28582244, 1):
        # for i in range(1, 100, ran_int):
        if (done is True):
            print('em')
            break

        pointer = i
        for rm in maps:
            stop = False
            for rmm in rm:
                [x, y, z] = rmm
                # print(x, y, z, pointer)
                # time.sleep(.1)

                if (stop is True):
                    continue
                for ss in rm:
                    x = ss[0]
                    y = ss[1]
                    if (x == pointer and stop is False):
                        pointer = y
                        stop = True
                if (stop is True):
                    continue
                if ((pointer > y + z) or pointer < y):
                    # print('>>', pointer)
                    continue

                elif (x > y):
                    pointer = abs(pointer - abs(x - y))
                else:
                    pointer += abs(x - y)
                # print('>>>>', pointer)

        print(cycles, ran_int, i, pointer)
        # print('========')

        for s_i, seed in enumerate(seeds):
            if (s_i % 2 == 0):
                seed_int = seed
                if (pointer >= seed_int and pointer <= seed_int + seeds[s_i + 1]):
                    print('GOTCHA', pointer)
                    result = i
                    done = True
                    break

# if ([0]) [1]
# if (>) +
# else -

# for s_i, seed in enumerate(seeds):
#     if (s_i % 2 == 0):
#         seed_int = int(seed)
#         for ii, j in enumerate(range(0, int(seeds[s_i + 1]))):

#             pointer = seed_int + ii
#             for mapa_i, mapa in enumerate(maps):
#                 # print('SECTION:', mapa_i)
#                 for ma in mapa:
#                     [d_r, s_r, r_l] = ma
#                     print(ma, pointer, (s_r + r_l) - pointer)
#                     # time.sleep(.1)
#                     if (pointer >= s_r and pointer <= s_r + r_l):
#                         diff = pointer - s_r
#                         # print('>>>', pointer, '->', d_r + diff)
#                         pointer = d_r + diff
#                         break

#             if (len(result) == 0):
#                 result.append(int(pointer))
#             elif (pointer < min(result)):
#                 result.append(int(pointer))
#             # print(ii, result)
#             print('==')


print(result)

assert test_result == result

# seeds: 3429320627 235304036 1147330745 114559245 1684000747 468955901 677937579 96599505 1436970021 26560102 3886049334 159534901 936845926 25265009 3247146679 95841652 3696363517 45808572 2319065313 125950148

# 1501654214
# 1439937237
# 531596735
# 240320250
# 629100001
# 378910001
# 378900950
# 28583346
# 28582244


# last stop
# 1228122
