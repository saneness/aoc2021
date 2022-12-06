from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
data = [item for item in puzzle.input_data.split("\n")]

n = len(data)

gamma = ""
epsilon = ""

for bit in range(len(data[0])):
    ones = sum([int(item[bit]) for item in data])
    if ones > n / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

data_temp = data.copy()
for bit in range(len(data_temp[0])):
    n = len(data_temp)
    if n > 1:
        ones = sum([int(item[bit]) for item in data_temp])
        zeroes = n - ones
        if zeroes != 0 and ones >= zeroes or zeroes == 0:
            data_temp = [item for item in data_temp if item[bit] == "1"]
        else:
            data_temp = [item for item in data_temp if item[bit] == "0"]


oxygen = data_temp[0]

data_temp = data.copy()
for bit in range(len(data_temp[0])):
    n = len(data_temp)
    if n > 1:
        ones = sum([int(item[bit]) for item in data_temp])
        zeroes = n - ones
        if zeroes != 0 and ones >= zeroes or zeroes == 0:
            data_temp = [item for item in data_temp if item[bit] == "0"]
        else:
            data_temp = [item for item in data_temp if item[bit] == "1"]

co2 = data_temp[0]

answer_a = int(gamma, 2) * int(epsilon, 2)
answer_b = int(oxygen, 2) * int(co2, 2)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b