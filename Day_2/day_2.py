"""AOC 2021 Day 2"""
# Calculate changes to global variables for part 1 based on rules
def calculate_1(cur_point):
    global HORIZONTAL
    global DEPTH

    if cur_point[0] == 'forward':
        HORIZONTAL += int(cur_point[1])
    elif cur_point[0] == 'down':
        DEPTH += int(cur_point[1])
    elif cur_point[0] == 'up':
        DEPTH -= int(cur_point[1])

# Calculate changes to global variables for part 2 based on rules
def calculate_2(cur_point):
    global HORIZONTAL
    global DEPTH
    global AIM

    if cur_point[0] == 'forward':
        HORIZONTAL += int(cur_point[1])
        DEPTH += (AIM * int(cur_point[1]))
    elif cur_point[0] == 'down':
        AIM += int(cur_point[1])
    elif cur_point[0] == 'up':
        AIM -= int(cur_point[1])

# Reset global parameters
def reset_parameters():
    global HORIZONTAL
    global DEPTH
    global AIM

    HORIZONTAL = DEPTH = AIM = 0

# Main program entry
values = [n.split() for n in open('C:/Data/GitHub/AOC_2021/Day_2/input.txt', 'r')]

HORIZONTAL = DEPTH = AIM = 0

for point in values:
    calculate_1(point)

print(HORIZONTAL * DEPTH)

reset_parameters()

for point in values:
    calculate_2(point)

print(HORIZONTAL * DEPTH)
