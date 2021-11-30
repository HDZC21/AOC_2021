"""Hello World and Day 1 of AOC 2020"""
OUT_MSG = "Hello World"
print(OUT_MSG)

input_file = open('C:/Data/GitHub/AOC_2021/Hello/AOC_2020_1_Input_File.txt', 'r')
input_file_lines = input_file.readlines()
# map applies the 'int' function to inputFileLines in an iterative manner, with Python 3.0 and later
# must be then converted to a list. turns out no need to convert to list.
input_file_values = list(map(int, input_file_lines))

# set removes duplicates and creates a hash map allowing for O(1) time complexity searching.
input_file_set = set(input_file_values)

for input_num in input_file_set:
    if 2020 - input_num in input_file_set:
        print (input_num * (2020 - input_num))
        break

# The for else loop is a unique Python construct. the else statement is only executed if the for
# statement terminates normally (not by a break), otherwise it is skipped.
# http://psung.blogspot.com/2007/12/for-else-in-python.html
for index, input_num_a in enumerate(input_file_values):
    for input_num_b in input_file_values[index + 1:]:
        if 2020 - input_num_a - input_num_b in input_file_set:
            print (input_num_a * input_num_b * (2020 - input_num_a - input_num_b))
            break
    else:
        continue
    break
