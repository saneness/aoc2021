from aocd.models import Puzzle
from statistics import median, mean

puzzle = Puzzle(year=2021, day=7)
data = [int(item) for item in puzzle.input_data.split(',')]

center = int(median(data))
bot = int(mean(data))
top = bot + 1
fuels = []
for point in [bot, top]:
    fuels.append(int(sum([abs(item-point)*(abs(item-point)+1)/2 for item in data])))

answer_a = sum([abs(item-center) for item in data])
answer_b = min(fuels)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b