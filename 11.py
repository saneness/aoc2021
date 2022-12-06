from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=11)
data = [[int(subitem) for subitem in item] for item in puzzle.input_data.split()]

def flashing(a):
    new = True
    flashed = []
    while new:
        for i in range(1, 11):
            for j in range(1, 11):
                if a[i][j] > 9 and (i, j) not in flashed:
                    flashed.append((i, j))
                    for di in (-1, 0, 1):
                        for dj in (-1, 0, 1):
                            a[i+di][j+dj] += 1
        new = False
        for i in range(1, 11):
            for j in range(1, 11):
                if a[i][j] > 9 and (i, j) not in flashed:
                    new = True
    for i in range(12):
        for j in range(12):
            if i in (0, 11) or j in (0, 11) or a[i][j] > 9:
                a[i][j] = 0
    return a, len(flashed)

ext = data.copy()
for item in ext:
    item.insert(0, 0)
    item.insert(len(item), 0)
ext.insert(0, [0] * 12)
ext.insert(len(ext), [0] * 12)

flashed = 0
step = 0
count = 0
while flashed < 100:
    step += 1
    flash = False
    for i in range(1, 11):
        for j in range(1, 11):
            ext[i][j] += 1
            if ext[i][j] > 9:
                flash = True
    if flash:
        ext, flashed = flashing(ext)
        if step < 101:
            count += flashed

answer_a = count
answer_b = step

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b