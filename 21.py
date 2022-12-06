from aocd.models import Puzzle
from functools import cache

puzzle = Puzzle(year=2021, day=21)
data = [int(item.split()[-1]) for item in puzzle.input_data.split("\n")]

def deterministic():
    def move(pos1, pos2, score1, score2, dice):
        pos1 = (pos1 + dice - 1) % 10 + 1
        score1 += pos1
        return pos1, pos2, score1, score2

    pos1, pos2 = data[0], data[1]
    score1, score2 = 0, 0
    rolled = 0
    dice = -3
    while max(score1, score2) < 1000:
        rolled += 3
        dice = (dice + 9) % 10
        pos2, pos1, score2, score1 = move(pos1, pos2, score1, score2, dice)
    return min(score1, score2) * rolled

def quantum():
    @cache
    def play(pos1, pos2, score1, score2):
        if score2 >= 21:
            return 0, 1
        else:
            wins1, wins2 = 0, 0
            for dice, num in [(3, 1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
                pos_new = (pos1 + dice - 1) % 10 + 1
                subwins2, subwins1 = play(pos2, pos_new, score2, score1 + pos_new)
                wins1, wins2 = wins1 + subwins1 * num, wins2 + subwins2 * num
        return wins1, wins2

    p1, p2 = data[0], data[1]
    wins = play(p1, p2, 0, 0)
    return max(wins)

answer_a = deterministic()
answer_b = quantum()

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b
