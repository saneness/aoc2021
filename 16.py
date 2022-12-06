from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=16)
data = puzzle.input_data

def parse(message):
    i = 0
    version = int(message[i:i+3], 2)
    i += 3
    type_id = int(message[i:i+3], 2)
    i += 3
    versions = version
    if type_id == 4:
        value = ""
        tag = 1
        while tag != 0:
            tag = int(message[i], 2)
            value += message[i:i+5][1:]
            i += 5
        value = int(value, 2)
    else:
        values = []
        length_type_id = int(message[i], 2)
        i += 1
        if length_type_id == 0:
            sub_length = int(message[i:i+15], 2)
            i += 15
            j = i + sub_length
            while i < j - 6:
                versions_sum, count, value = parse(message[i:j])
                i += count
                versions += versions_sum
                values.append(value)
        elif length_type_id == 1:
            sub_count = int(message[i:i+11], 2)
            i += 11
            for _ in range(sub_count):
                versions_sum, count, value = parse(message[i:])
                i += count
                versions += versions_sum
                values.append(value)

        match type_id:
            case 0:
                value = sum(values)
            case 1:
                value = 1
                for item in values:
                    value *= item
            case 2:
                value = min(values)
            case 3:
                value = max(values)
            case 5:
                value = int(values[0] > values[1])
            case 6:
                value = int(values[0] < values[1])
            case 7:
                value = int(values[0] == values[1])

    return versions, i, value

spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=len(data)*4, type='b')
message = format(int(data, 16), spec)
versions, _, values = parse(message)

answer_a = versions
answer_b = values

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b