data = [int(item) for item in open("data/6.data").read().split(',')]

def solve():
    def populate(day):
        init = [sum([1 for item in data if item == i]) for i in range(9)]
        population = init.copy()
        for _ in range(day):
            new = population.pop(0)
            population[6] += new
            population.append(new)
        return sum(population)

    print(populate(80))
    print(populate(256))


solve()