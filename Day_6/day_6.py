"""AOC 2021 Day 6"""

input_values = [n.split(',') for n in open('C:/Data/GitHub/AOC_2021/Day_6/input.txt', 'r')]
input_values = [int(n) for n in input_values[0]]

fishes = [0]*9

for input_val in input_values:
    fishes[input_val] += 1

print(fishes)

for _ in range(1, 257):
    new_fish = fishes[0]
    for idx in range(0, len(fishes)-1):
        fishes[idx] = fishes[idx+1]
    fishes[8] = new_fish
    fishes[6] = fishes[6] + new_fish

print(sum(fishes))
