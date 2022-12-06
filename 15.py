from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=15)
data = puzzle.input_data.split("\n")

def get_risks(a):
    x_size = len(a[0])
    y_size = len(a)
    risks = {(x, y): -1 for x in range(x_size) for y in range(y_size)}
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move = lambda pos, dir: tuple([x + y for (x, y) in zip(pos, dir)])
    pos = (0, 0)
    risks.update({pos: 0})
    is_continue = True
    visited = {(x, y): False for x in range(x_size) for y in range(y_size)}
    while is_continue:
        is_continue = False
        for pos in risks:
            if not visited[pos]:
                visited[pos] = True
                for dir in dirs:
                    next = move(pos, dir)
                    if next[0] < y_size and next[1] < x_size and next[0] > -1 and next[1] > -1:
                        if risks[next] == -1:
                            risks.update({next: risks.get(pos) + int(a[next[0]][next[1]])})
                            is_continue = True
                        else:
                            if risks.get(next) > risks.get(pos) + int(a[next[0]][next[1]]):
                                risks.update({next: risks.get(pos) + int(a[next[0]][next[1]])})
                                visited[next] = False
                                is_continue = True
    return risks[(x_size - 1, y_size - 1)]

x_size = len(data[0])
ext = []
ext_rows = []
for row in data:
    ext_row = row
    for i in range(x_size - 1):
        ext_row += "".join([str(((int(item) + i) % 9) + 1) for item in row])
    ext_rows.append(ext_row)
for i in range(5):
    for row in ext_rows:
        ext.append(row[i*x_size:(i+5)*x_size])

answer_a = get_risks(data)
answer_b = get_risks(ext)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b