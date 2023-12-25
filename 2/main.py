lines = []
file_path = './input.txt'
# file_path = './test.txt'
test_result = 2286
a = '12 red, 13 green, 14 blue'
red = 12
green = 13
blue = 14

with open(file_path) as f:
    lines = [line.rstrip('\n') for line in f]

result = 0
for line in lines:
  arr = line.split(': ')
  game_id = int(arr[0].split(' ')[1])
  rounds = arr[1].split('; ')

  rounds_map = []
  for round in rounds:
    temp = round.split(', ')
    for x in temp:
      y = x.split(' ') 
      rounds_map.append([y[1], y[0]])

  # game_valid = True
  max_red = float('-inf')
  max_green = float('-inf')
  max_blue = float('-inf')

  for rm in rounds_map:
    local_red = 0
    local_green = 0
    local_blue = 0

    color = rm[0]
    value = int(rm[1])

    # if (color == 'red'):
    #   local_red += value
    # elif (color == 'green'):
    #   local_green += value
    # elif (color == 'blue'):
    #   local_blue += value

    if (color == 'red' and value > max_red):
      max_red = value
    elif (color == 'green' and value > max_green):
      max_green = value
    elif (color == 'blue' and value > max_blue):
      max_blue = value


    # print(local_red, local_green, local_blue)
    # if (red < local_red or green < local_green or blue < local_blue):
    #   print('NOT VALID')
    #   game_valid = False
    #   break


  print(max_red * max_green * max_blue)
 
  result += (max_red * max_green * max_blue)
  # if (game_valid):
  #   print('ADD', result, game_id)
  #   result += game_id

  print('===========')


print(result)
assert test_result == result