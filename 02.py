from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)
data = [(item.split()[0], int(item.split()[1])) for item in puzzle.input_data.split("\n")]

horizontal = 0
depth = 0
aim = 0
depth_aimed = 0

for item in data:
    dir, val = item[0], item[1]
    if dir == "down":
        aim += val
        depth += val
    elif dir == "up":
        aim -= val
        depth -= val
    elif dir == "forward":
        horizontal += val
        depth_aimed += aim * val

answer_a = horizontal * depth
answer_b = horizontal * depth_aimed

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b