"""AOC 2021 Day 3"""
import statistics
from statistics import mode
from statistics import multimode

def reduce_input(input_list, search_idx, search_val):
    reduced_list = [elem for elem in input_list if elem[search_idx] == search_val]
    return reduced_list

def find_occurances_of_bit(input_list, search_val, bit_mode):
    idx = 0
    while len(input_list) > 1 and idx < len(input_list[0]) - 1:
        input_list = reduce_input(input_list, idx, search_val)
        input_cols = list(zip(*input_list))
        
        mode = multimode(input_cols[idx+1])
        mul_mode = bool(len(mode) > 1)

        if bit_mode == 'MOB':
              if mul_mode:
                  search_val = '1'
              else:
                  search_val = str(mode[0])
        else:
              if mul_mode:
                  search_val = '0'
              else:
                  search_val = str(1 - int(mode[0]))
        idx += 1
    
    if len(input_list) > 1:
        input_list = reduce_input(input_list, idx, search_val)
    return input_list

# Main program entry

input_values = [n.rstrip('\n') for n in open('C:/Data/GitHub/AOC_2021/Day_3/input.txt', 'r')]

# Part 1
# https://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists
input_columns = list(zip(*input_values))

gamma_rate = [mode(column) for column in input_columns]

ogr_init_col = gamma_rate[0]
c02_init_col = str(1-int(ogr_init_col))

epsilon_rate = ''.join([str(1-int(elem)) for elem in gamma_rate])
gamma_rate = ''.join(gamma_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2
ogr_list = find_occurances_of_bit(input_values, ogr_init_col, 'MOB')
c02_list = find_occurances_of_bit(input_values, c02_init_col, 'LOB')

print(int(ogr_list[0], 2) * int(c02_list[0], 2))
