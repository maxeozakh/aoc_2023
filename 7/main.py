file_path = './input.txt'
# file_path = './test.txt'
test_result = 5905
r_a = []
r = 0
weights = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}


def is_x_k(h, x):
    for symbol in h:
        counter = 0
        for c in h:
            if (c is symbol or c is 'J'):
                counter += 1

        if (counter == x):
            return True

    return False


def is_5(h):
    return is_x_k(h, 5)


def is_4(h):
    return is_x_k(h, 4) and not is_x_k(h, 5)


def is_3(h):
    return is_x_k(h, 3) and not is_x_k(h, 4)


assert is_5('kxkkk') == False
assert is_5('kkkkk') == True
assert is_5('kkkJk') == True
assert is_5('kkJJJ') == True

assert is_4('kkxkk') == True
assert is_4('kkkkz') == True
assert is_4('kkkkk') == False
assert is_4('kkxxx') == False
assert is_4('xkkkk') == True
assert is_4('xkkJk') == True
assert is_4('xkkxk') == False

assert is_3('xkkxk') == True
assert is_3('kkxxa') == False
assert is_3('kkxxJ') == True


def is_fh(h):
    dict = {}

    for c in h:
        if (c in dict.keys()):
            dict[c] += 1
        else:
            dict[c] = 1

    if (len(dict.keys()) == 3 and ('J' in dict.keys())):
        return True
    return len(dict.keys()) == 2 and ((dict.values()[0] == 2 and dict.values()[1] == 3) or (dict.values()[0] == 3 and dict.values()[1] == 2))


assert is_fh('kk111') == True
assert is_fh('kk111') == True
assert is_fh('k1k11') == True
assert is_fh('11k11') == False
assert is_fh('11k1J') == True
assert is_fh('11JJJ') == True


def is_x_pair(h, x):
    counter = 0
    dict = {}

    for cart in h:
        if (cart in dict.keys()):
            dict[cart] += 1
            if (dict[cart] == 2):
                counter += 1
        elif (cart == 'J'):
            counter += 1
        else:
            dict[cart] = 1

    return counter == x and len(dict.keys()) == 5 - x


def is_two_pair(h):
    return is_x_pair(h, 2)


assert is_two_pair('kk111') == False
assert is_two_pair('kk11x') == True
assert is_two_pair('xk11o') == False
assert is_two_pair('xzav1') == False
assert is_two_pair('11222') == False
assert is_two_pair('11223') == True


def is_pair(h):
    return is_x_pair(h, 1)


assert is_pair('xx11o') == False
assert is_pair('xx1zo') == True
assert is_pair('xx1zx') == False
assert is_pair('x11zx') == False
assert is_pair('x91zx') == True


def is_high(h):
    return is_x_pair(h, 0)


assert is_high('xx11o') == False
assert is_high('xx1zo') == False
assert is_high('xx1zx') == False
assert is_high('x11zx') == False
assert is_high('x91zx') == False
assert is_high('12345') == True


def get_rank_by_str(hand):
    if (is_5(hand)):
        return 1
    if (is_4(hand)):
        return 2
    if (is_fh(hand)):
        return 3
    if (is_3(hand)):
        return 4
    if (is_two_pair(hand)):
        return 5
    if (is_pair(hand)):
        return 6
    if (is_high(hand)):
        return 7


assert get_rank_by_str('kkkkk') == 1
assert get_rank_by_str('kkxkk') == 2
assert get_rank_by_str('k1k11') == 3
assert get_rank_by_str('xkkxk') == 3
assert get_rank_by_str('xkaxx') == 4
assert get_rank_by_str('aazxx') == 5
assert get_rank_by_str('zazxx') == 5
assert get_rank_by_str('0adxx') == 6
assert get_rank_by_str('0adx1') == 7
assert get_rank_by_str('J2A5T') == 6
assert get_rank_by_str('JxzXT') == 6
assert get_rank_by_str('zJzTT') == 3


def get_group_by_combo_str(data):
    dict = {}

    for line in data:
        [hand, bet] = line.split(' ')
        rank = get_rank_by_str(hand)

        if (rank in dict.keys()):
            dict[rank].append(line)
        else:
            dict[rank] = [line]

    return dict


def to_numbers(symbol):
    if (type(symbol) is int):
        return symbol
    elif (symbol.isdigit()):
        return int(symbol)
    elif (not symbol.isdigit()):
        return weights[symbol]


def estimate_by_symbol(first, second):
    # extract hands from data
    first_h = first.split(' ')[0]
    second_h = second.split(' ')[0]
    result = []
    for i, s in enumerate(first_h):
        f_s = to_numbers(first_h[i])
        s_s = to_numbers(second_h[i])

        if (f_s > s_s):
            return [first, second, '']
        elif (f_s < s_s):
            return [second, first, '']

        if (i == len(first_h) - 1):
            return [first, second, 'e']


lines = []
with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]

# for line in lines:
#     print(line)
#     print('===========')

groups = get_group_by_combo_str(lines)
# print('groups: ', groups)

cursed = list(reversed(groups.keys()))
rank = []
counter = 1
for key in cursed:

    group = groups[key]
    # print('group: ', group)

    group_rating = {}
    for hand in group:
        hand = hand
        group_rating[hand] = 0

    if (len(group) == 1):
        group_rating[group[0]] = counter

    else:
        for i, hand_data in enumerate(group):
            for j, compare_hand_data in enumerate(group):
                if (i == j):
                    continue

                # print('pair', hand_data, compare_hand_data)
                # print('group rating', group_rating)
                # print('group', group)
                # print('Before estimate: ', hand_data, compare_hand_data)
                pair = estimate_by_symbol(hand_data, compare_hand_data)
                # print('After estimate', pair)
                # print('')

                [winner, loser, sign] = pair
                if (sign == 'e'):
                    continue
                else:
                    group_rating[winner] += 1

    # print('Group rating: ', group_rating)
    sorted_rating = sorted(group_rating.items(),
                           key=lambda x: x[1], reverse=False)

    sorted_dict = {}
    for i, x in enumerate(sorted_rating):
        current_hand_data = sorted_rating[i][0]

        sorted_dict[current_hand_data] = counter

        # do not increase counter if pair a equal
        if (i != len(sorted_rating) - 1):
            current_hand = current_hand_data.split(' ')[0]
            next_hand_data = sorted_rating[i + 1][0]
            next_hand = next_hand_data.split(' ')[0]

            pair = estimate_by_symbol(current_hand, next_hand)
            # print(current_hand, next_hand)
            [winner, loser, sign] = pair
            if (sign == 'e'):
                print('mm', winner, loser)
                continue

        counter += 1

    sorted_rating = sorted(sorted_dict.items(),
                           key=lambda x: x[1], reverse=False)
    print('Sorted rating: ', sorted_rating)
    print('*')
    for hand in sorted_rating:
        rank.append(hand)


print('========')

# print(rank)
for i, data in enumerate(rank):
    # print(data, data[1])
    r += int(data[0].split(' ')[1]) * data[1]


print(r)
assert test_result == r
