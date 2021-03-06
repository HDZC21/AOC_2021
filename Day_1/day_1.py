"""AOC 2021 Day 1"""
values = [int(n) for n in open('C:/Data/GitHub/AOC_2021/Day_1/input.txt', 'r')]

NUM_INCREASES = 0
# Unexpected (to me) behaviour, val enumerates from 1..n, index is still 0..n-1
for index, val in enumerate(values[1:]):
    if val > values[index]:
        NUM_INCREASES += 1

print(NUM_INCREASES)

NUM_INCREASES = 0

# Create list of lists of custom overlapping size from single list
# https://www.geeksforgeeks.org/python-convert-list-to-custom-overlapping-nested-list/

# List comprehension
# https://www.w3schools.com/python/python_lists_comprehension.asp

# range(a, b, c) function creates a sequence of numbers from a to b in steps of
# c (default step is 1)

# [index: index + 3] must be index safe as does not throw 'out of bounds' error when
# index = n-2, n-1 or n
tuples = [tuple(values[index: index + 3]) for index in range(0, len(values))]

for index, val in enumerate(tuples[1:]):
    if sum(list(val)) > sum(list(tuples[index])):
        NUM_INCREASES += 1

print(NUM_INCREASES)
