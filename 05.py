from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=5)
data = [[int(subitem) for subitem in item.split(' -> ')[0].split(',')] + [int(subitem) for subitem in item.split(' -> ')[1].split(',')] for item in puzzle.input_data.split('\n')]

def overlaps(diagonal):
    sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)
    size = max([max(item) for item in data]) + 1
    a = [[0 for i in range(size)] for j in range(size)]
    for item in data:
        if item[0] == item[2] or item[1] == item[3]:
            x_diff = item[2] - item[0]
            x_step = sign(x_diff)
            y_diff = item[3] - item[1]
            y_step = sign(y_diff)
            for i in range(abs(x_diff) + 1):
                for j in range(abs(y_diff) + 1):
                    a[item[1]+y_step*j][item[0]+x_step*i] += 1
        elif diagonal:
            x_diff = item[2] - item[0]
            x_step = sign(x_diff)
            y_diff = item[3] - item[1]
            y_step = sign(y_diff)
            for i in range(abs(x_diff) + 1):
                a[item[1]+y_step*i][item[0]+x_step*i] += 1
    return sum(sum([1 for subitem in item if subitem >= 2]) for item in a)

answer_a = overlaps(diagonal=False)
answer_b = overlaps(diagonal=True)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b