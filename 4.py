from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=4)
data = [item for item in puzzle.input_data.split('\n\n')]

def check(bingo):
    for i in range(5):
        row = bingo[i*5:i*5+5]
        col = bingo[i:][::5]
        if sum(row) == -5 or sum(col) == -5:
            return True
    return False

numbers = [int(item) for item in data[0].split(',')]
bingos = [[int(subitem) for subitem in item.split()] for item in data[1:]]
winner_number = -1
winner_bingo = []
first_number = -1
first_bingo = []

count = len(bingos)
winner_count = [0] * count

for number in numbers:
    for i in range(count):
        if number in bingos[i]:
            bingos[i][bingos[i].index(number)] = -1

            if check(bingos[i]):
                winner_count[i] = 1
                winner_number = number
                winner_bingo = bingos[i].copy()

    if winner_number != -1 and first_number == -1:
        first_number = winner_number
        first_bingo = winner_bingo.copy()

    bingos = [bingo for bingo in bingos if winner_count[bingos.index(bingo)] != 1]
    count = len(bingos)
    winner_count = [0] * count

answer_a = first_number * sum([item for item in first_bingo if item > 0])
answer_b = winner_number * sum([item for item in winner_bingo if item > 0])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b