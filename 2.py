data = [(item.split()[0], int(item.split()[1])) for item in open("data/2.data").read().split("\n")]

def solve():
    horizontal = 0
    depth = 0
    aim = 0
    depth_aimed = 0

    for item in data:
        dir, val = item[0], item[1]
        if dir == "down":
            aim += val
            depth += val
        elif dir == "up":
            aim -= val
            depth -= val
        elif dir == "forward":
            horizontal += val
            depth_aimed += aim * val

    print(horizontal * depth)
    print(horizontal * depth_aimed)


solve()