from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)
data = [int(item) for item in puzzle.input_data.split()]

def larger(size):
    count = 0
    prev = data[0]
    for i in range(1, len(data) - size + 1):
        if data[i+size-1] > prev:
            count +=1
        prev = data[i]
    return count

answer_a = larger(1)
answer_b = larger(3)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b