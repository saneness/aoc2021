from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=6)
data = [int(item) for item in puzzle.input_data.split(',')]

def populate(day):
    init = [sum([1 for item in data if item == i]) for i in range(9)]
    population = init.copy()
    for _ in range(day):
        new = population.pop(0)
        population[6] += new
        population.append(new)
    return sum(population)

answer_a = populate(80)
answer_b = populate(256)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b