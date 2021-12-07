"""AOC 2021 Day 7"""

import statistics
from statistics import mode

def nth_triangle_number(n):
    if n == 0:
        return 0
    else:
        return ((n*(n+1)/2))

input_values = [n.split(',') for n in open('C:/Data/GitHub/AOC_2021/Day_7/input.txt', 'r')]
input_values = [int(n) for n in input_values[0]]

fuel_spent = []
for idx in range(min(input_values), max(input_values)+1):
    fuel_spent.append(sum([abs(idx - n) for n in input_values]))

min_fuel_spend = min(fuel_spent)
print(min_fuel_spend)

non_constant_fuel_spent = []
for idx in range(min(input_values), max(input_values)+1):
    non_constant_fuel_spent.append(sum([nth_triangle_number(abs(idx - n)) for n in input_values]))

min_non_constant_fuel_spend = min(non_constant_fuel_spent)
print(int(min_non_constant_fuel_spend))