from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)
data = puzzle.input_data.split()

rules = {"(": ")", "[": "]", "{": "}", "<": ">"}
corrupted_rules = {")": 3, "]": 57, "}": 1197, ">": 25137}
corrupted_score = 0
complete_rules = {")": 1, "]": 2, "}": 3, ">": 4}
complete_scores = []
for item in data:
    chunks = []
    for i in range(len(item)):
        if item[i] in ("(", "[", "{", "<"):
            chunks.append(item[i])
        elif item[i] in (")", "]", "}", ">"):
            if rules[chunks[-1]] == item[i]:
                chunks.pop()
            else:
                corrupted_score += corrupted_rules[item[i]]
                break
        if i == len(item) - 1:
            score = 0
            points = reversed([complete_rules[rules[chunk]] for chunk in chunks])
            for point in points:
                score *= 5
                score += point
            complete_scores.append(score)

answer_a = corrupted_score
answer_b = sorted(complete_scores)[int((len(complete_scores) - 1) / 2)]

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b