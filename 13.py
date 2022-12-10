from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=13)
data = puzzle.input_data.split("\n\n")
data = [[[int(subitem) for subitem in item.split(",")] for item in data[0].split("\n")], [[item.split()[-1].split("=")[0], int(item.split()[-1].split("=")[1])] for item in data[1].split("\n")]]

def fold(paper, axis, line):
    if axis == "y":
        first = paper[:line]
        second = paper[line+1:][::-1]
    elif axis == "x":
        first = [item[:line] for item in paper]
        second = [item[line+1:][::-1] for item in paper]
    else:
        print("Error")
    for i in range(len(first)):
        for j in range(len(first[0])):
            if second[i][j] == "#":
                first[i][j] = "#"
    return first

def decode(coded):
    decoder = {
        "111110-001001-001001-111110": "A",
        "111111-100101-100101-011010": "B",
        "011110-100001-100001-010010": "C",
        # "": "D",
        "111111-100101-100101-100001": "E",
        "111111-000101-000101-000001": "F",
        "011110-100001-101001-111010": "G",
        "111111-000100-000100-111111": "H",
        # "": "I",
        "010000-100000-100001-011111": "J",
        "111111-000100-011010-100001": "K",
        "111111-100000-100000-100000": "L",
        # "": "M",
        # "": "N",
        "011110-100001-100001-011110": "O",
        "111111-001001-001001-000110": "P",
        "011110-100001-100011-011111": "Q",
        "111111-001001-011001-100110": "R",
        "010010-100101-101001-010010": "S",
        # "": "T",
        "011111-100000-100000-011111": "U",
        # "": "V",
        # "": "W",
        # "": "X",
        # "": "Y",
        "110001-101001-100101-100011": "Z"
    }

    coded_list = []
    for i in range(len(coded[0]) // 5):
        temp = []
        for j in range(4):
            temp.append("".join([coded[k][i*5+j] for k in range(6)][::-1]).replace("#", "1").replace(".", "0"))
        coded_list.append("-".join(temp))

    return "".join(decoder[coded] for coded in coded_list)

dots = data[0]
folds = data[1]

x_size, y_size = max(dot[0] for dot in dots) + 1, max(dot[1] for dot in dots) + 1
paper = [["." for x in range(x_size)] for y in range(y_size)]

for dot in dots:
    paper[dot[1]][dot[0]] = "#"

for line in folds[:1]:
    paper = fold(paper, axis=line[0], line=line[1])

after_first = sum([sum([1 for col in row if col == "#"]) for row in paper])

for line in folds[1:]:
    paper = fold(paper, axis=line[0], line=line[1])

answer_a = after_first
answer_b = decode(paper)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b
