msg = "Hello World"
print(msg)

inputFile = open('C:/Data/GitHub/AOC_2021/Hello/AOC_2020_1_Input_File.txt', 'r')
inputFileLines = inputFile.readlines()

values = [0] * 2020
print(len(values))

for inputNum in inputFileLines:
  inputInt = int(inputNum)
  if (values[(2019 - inputInt)] == 1):
    print(((2019 - inputInt) + 1) * inputInt)
  else:
    values[inputInt - 1] = 1