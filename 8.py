data = [item.split() for item in open("data/8.data").read().replace('| ', '').split('\n')]

def solve():
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

    print(unique_digits)
    print(sum(numbers))


solve()