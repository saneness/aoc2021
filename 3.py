data = [item for item in open("data/3.data").read().split("\n")]

def solve():

    n = len(data)

    gamma = ""
    epsilon = ""

    for bit in range(len(data[0])):
        ones = sum([int(item[bit]) for item in data])
        if ones > n / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    data_temp = data.copy()
    for bit in range(len(data_temp[0])):
        n = len(data_temp)
        if n > 1:
            ones = sum([int(item[bit]) for item in data_temp])
            zeroes = n - ones
            if zeroes != 0 and ones >= zeroes or zeroes == 0:
                data_temp = [item for item in data_temp if item[bit] == "1"]
            else:
                data_temp = [item for item in data_temp if item[bit] == "0"]


    oxygen = data_temp[0]

    data_temp = data.copy()
    for bit in range(len(data_temp[0])):
        n = len(data_temp)
        if n > 1:
            ones = sum([int(item[bit]) for item in data_temp])
            zeroes = n - ones
            if zeroes != 0 and ones >= zeroes or zeroes == 0:
                data_temp = [item for item in data_temp if item[bit] == "0"]
            else:
                data_temp = [item for item in data_temp if item[bit] == "1"]

    co2 = data_temp[0]

    power_consumption = int(gamma, 2) * int(epsilon, 2)
    life_support = int(oxygen, 2) * int(co2, 2)

    print(power_consumption)
    print(life_support)


solve()