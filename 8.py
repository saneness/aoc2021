from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)
data = [item.split() for item in puzzle.input_data.replace('| ', '').split('\n')]

unique_digits = sum(sum([1 for subitem in item[-4:] if len(subitem) in (2, 3, 4, 7)]) for item in data)
shared = lambda first, second: sum([1 for symbol in first if symbol in second])
numbers = []
for item in data:
    decoded = {}
    # 1 4 7 8
    for value in item:
        segments = len(value)
        if segments == 2:
            one = value
            decoded.update({value: 1})
        elif segments == 4:
            four = value
            decoded.update({value: 4})
        elif segments == 3:
            decoded.update({value: 7})
        elif segments == 7:
            decoded.update({value: 8})
    # 0 2 3 5 6 9
    for value in item:
        shared_one = shared(one, value)
        shared_four = shared(four, value)
        segments = len(value)
        if shared_one == 2 and shared_four == 3 and segments == 6:
            decoded.update({value: 0})
        elif shared_one == 1 and shared_four == 2 and segments == 5:
            decoded.update({value: 2})
        elif shared_one == 2 and shared_four == 3 and segments == 5:
            decoded.update({value: 3})
        elif shared_one == 1 and shared_four == 3 and segments == 5:
            decoded.update({value: 5})
        elif shared_one == 1 and shared_four == 3 and segments == 6:
            decoded.update({value: 6})
        elif shared_one == 2 and shared_four == 4 and segments == 6:
            decoded.update({value: 9})
    numbers.append(int(''.join([str(decoded[subitem]) for subitem in item[-4:]])))

answer_a = unique_digits
answer_b = sum(numbers)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b