data = [int(item) for item in open("data/7.data").read().split(',')]

from statistics import median, mean

def solve():
    center = int(median(data))
    bot = int(mean(data))
    top = bot + 1
    fuels = []
    for point in [bot, top]:
        fuels.append(int(sum([abs(item-point)*(abs(item-point)+1)/2 for item in data])))

    print(sum([abs(item-center) for item in data]))
    print(min(fuels))


solve()