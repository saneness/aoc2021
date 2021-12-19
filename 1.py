data = [int(item) for item in open("data/1.data").read().split()]

def solve():
    def larger(size):
        count = 0
        prev = data[0]
        for i in range(1, len(data) - size + 1):
            if data[i+size-1] > prev:
                count +=1
            prev = data[i]
        return count

    print(larger(1))
    print(larger(3))


solve()