from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=14)
data = puzzle.input_data.split("\n\n")
data = [data[0], {item.split(" -> ")[0]: item.split(" -> ")[1] for item in data[1].split("\n")}]

def polymerize(steps):
    template = data[0]
    rules = {}
    for rule in data[1]:
        rules.update({rule: [rule[0] + data[1][rule], data[1][rule] + rule[1]]})
    freq = {rule: template.count(rule) for rule in rules}
    for _ in range(steps):
        freq_new = {}
        for item in freq:
            if freq[item] > 0:
                for rule in rules[item]:
                    freq_new.update({rule: freq_new.get(rule, 0) + freq[item]})
        freq = freq_new
    freq_total = {template[0]: 0.5, template[-1]: 0.5}
    for item in freq:
        for subitem in item:
            freq_total.update({subitem: freq_total.get(subitem, 0) + freq[item] / 2})
    return int(max(freq_total.values()) - min(freq_total.values()))

answer_a = polymerize(10)
answer_b = polymerize(40)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b