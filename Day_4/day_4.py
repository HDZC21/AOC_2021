"""AOC 2021 Day 4"""

from os import replace


input_values = [n.rstrip('\n') for n in open('C:/Data/GitHub/AOC_2021/Day_4/sample_input.txt', 'r')]

moves = input_values[0].split(',')
input_values.pop(0)
input_values.pop(0)

grids = [val.split(' ') for val in input_values]
clean_grids = []

for list_val in grids:
    list_val = [elem for elem in list_val if elem != '']
    if list_val != []:
        clean_grids.append(list_val)
    #print(list_val)
#grids = [elem for elem in grids if elem != 'x']
#grids = [int(val) for val in grids]

#print(input_values)
#print(moves)
#print(clean_grids)
num_rows = len(clean_grids[0])
num_boards = int(len(clean_grids)/num_rows)
game_boards = [[[]]]
append_idx = 0
for idx in range(num_boards):
    game_boards.append([])
    for idxx in range(num_rows):
        game_boards[idx].append([])
        game_boards[idx][idxx].append(clean_grids[append_idx])
        append_idx += 1

print(game_boards)