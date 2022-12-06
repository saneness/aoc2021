from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=17)
data =[[int(subitem) for subitem in item.split("=")[-1].split("..")] for item in puzzle.input_data.split(",")]

x_min = data[0][0]
x_max = data[0][1]
y_min = data[1][0]
y_max = data[1][1]

count = 0
max = 0

for x_start in range(x_max + 1):
    max_current = 0
    for y_start in range(y_min - 1, 1 - y_min):
        x = 0
        y = 0
        x_current = x_start
        y_current = y_start
        prev = [0, 0]
        while not (x > x_max or y < y_min):
            prev = [x, y]
            x += x_current
            y += y_current
            if y > max_current:
                max_current = y
            x_current -= 1 if x_current > 0 else 0
            y_current -= 1
        if prev[0] >= x_min and prev[0] <= x_max and prev[1] >= y_min and prev[1] <= y_max:
            count += 1
            if max_current > max:
                max = max_current

answer_a = max
answer_b = count

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b