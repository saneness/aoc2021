from aocd.models import Puzzle
from math import prod

puzzle = Puzzle(year=2021, day=9)
data = puzzle.input_data.split()

def basin(a, i, j):
    points = []
    points.append((i, j))
    if a[i][j] < a[i-1][j] and a[i-1][j] != "9":
        for point in basin(a, i-1, j):
            points.append(point)
    if a[i][j] < a[i+1][j] and a[i+1][j] != "9":
        for point in basin(a, i+1, j):
            points.append(point)
    if a[i][j] < a[i][j-1] and a[i][j-1] != "9":
        for point in basin(a, i, j-1):
            points.append(point)
    if a[i][j] < a[i][j+1] and a[i][j+1] != "9":
        for point in basin(a, i, j+1):
            points.append(point)
    return list(set(points))

ext = data.copy()
ext = [item.join(["9"]*2) for item in ext]
x_size = len(ext[0])
ext = ["9"*x_size] + ext + ["9"*x_size]
y_size = len(ext)
low_points = 0
basins = []
for i in range(1, y_size - 1):
    for j in range(1, x_size - 1):
        if ext[i][j] < ext[i-1][j] and \
            ext[i][j] < ext[i+1][j] and \
            ext[i][j] < ext[i][j-1] and \
            ext[i][j] < ext[i][j+1]:
            low_points += 1 + int(ext[i][j])
            basins.append(len(basin(ext, i, j)))

answer_a = low_points
answer_b = prod(sorted(basins)[-3:])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b