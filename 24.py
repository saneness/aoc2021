from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=24)
data = [item.split() for item in puzzle.input_data.split("\n")]

#      0    1    2    3    4    5    6    7    8    9   10   11   12   13
# a [  1,   1,   1,   1,  26,   1,   1,  26,   1,  26,  26,  26,  26,  26]
# b [ 12,  11,  10,  10, -16,  14,  12,  -4,  15,  -7,  -8,  -4, -15,  -8]
# c [  6,  12,   5,  10,   7,   0,   4,  12,  14,  13,  10,  11,   9,   9]
# a = [int(item[2]) for item in data if data.index(item) % 18 == 4]
# b = [int(item[2]) for item in data if data.index(item) % 18 == 5]
# c = [int(item[2]) for item in data if data.index(item) % 18 == 15]

def validate(w):
    w[4] = w[3] - 6
    w[7] = w[6]
    w[9] = w[8] + 7
    w[10] = w[5] - 8
    w[11] = w[2] + 1
    w[12] = w[1] - 3
    w[13] = w[0] - 2
    return w

#                 0  1  2  3  4  5  6  7  8  9 10 11 12 13
w_max = validate([9, 9, 8, 9, 0, 9, 9, 0, 2, 0, 0, 0, 0, 0])
w_min = validate([3, 4, 1, 7, 0, 9, 1, 0, 1, 0, 0, 0, 0, 0])

answer_a = ''.join(map(str, w_max))
answer_b = ''.join(map(str, w_min))

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b