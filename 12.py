data = [item.split("-") for item in open("data/12.data").read().split("\n")]

def solve():
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

    print(len(get_paths(cavemap, ["start"], 1)))
    print(len(get_paths(cavemap, ["start"], 2)))

solve()