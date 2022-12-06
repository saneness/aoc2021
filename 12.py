from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=12)
data = [item.split("-") for item in puzzle.input_data.split("\n")]

def get_paths(cavemap, path, small):
    result = [path]
    if path[-1] in cavemap:
        for next in cavemap[path[-1]]:
            counts = [sum([1 for item in path if item == cave]) for cave in cavemap if cave.upper() != cave]
            if next.upper() == next or next not in path or small not in counts:
                for item in get_paths(cavemap, path + [next], small):
                    result.append(item)
    return [path for path in result if path[-1] == "end"]

cavemap = {}
for item in data:
    if item[1] != "start" and item[0] != "end":
        cavemap.update({item[0]: cavemap.get(item[0], []) + [item[1]]})
    if item[0] != "start" and item[1] != "end":
        cavemap.update({item[1]: cavemap.get(item[1], []) + [item[0]]})

answer_a = len(get_paths(cavemap, ["start"], 1))
answer_b = len(get_paths(cavemap, ["start"], 2))

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b