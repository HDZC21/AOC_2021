"""AOC 2021 Day 1"""
values = [int(n) for n in open('C:/Data/GitHub/AOC_2021/Day_1/input.txt', 'r')]

# Sum of all instances where val[n] > val[n-1]
print(sum([1 for index,val in enumerate(values[1:]) if val > values[index]]))

# Sum of all instances where val[n] > val[n-4]. This is a mathematical optimisiation
# of the rolling window. 
print(sum([1 for index,val in enumerate(values[3:]) if val > values[index]]))