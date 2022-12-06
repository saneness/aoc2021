from aocd.models import Puzzle
from math import floor, ceil
import re

puzzle = Puzzle(year=2021, day=18)
data = puzzle.input_data.split()

def add(x, y):
    return "[" + x + "," + y + "]"

def is_nested(number):
    nested = 0
    i = 0
    while i < len(number):
        if number[i] == "[":
            nested += 1
        elif number[i] == "]":
            nested -= 1
        i += 1
        if nested > 4:
            while number[i] != "]":
                i += 1
            end = i
            while number[i] != "[":
                i -= 1
            start = i
            return (start, end + 1)
    return False

def explode(number, nested):
    nested_left = int(number[nested[0]+1:nested[1]-1].split(",")[0])
    nested_right = int(number[nested[0]+1:nested[1]-1].split(",")[1])
    left = nested[0] - 1
    right = nested[1] + 1
    while left >= 0:
        if left < 0:
            break
        elif number[left].isdigit():
            left_end = left + 1
            while number[left].isdigit():
                left -= 1
            left_start = left + 1
            break
        else:
            left -= 1
    while right < len(number):
        if right >= len(number):
            break
        elif number[right].isdigit():
            right_start = right
            while number[right].isdigit():
                right += 1
            right_end = right
            break
        else:
            right += 1
    exploded = ""
    if left >= 0:
        exploded += number[:left_start] + str(int(number[left_start:left_end]) + nested_left) + number[left_end:nested[0]]
    else:
        exploded += number[:nested[0]]
    exploded += "0"
    if right < len(number):
        exploded += number[nested[1]:right_start] + str(int(number[right_start:right_end]) + nested_right) + number[right_end:]
    else:
        exploded += number[nested[1]:]
    return exploded

def is_big(number):
    big = re.search("\d\d+", number)
    if big:
        return big.span()
    return False

def split(number, big):
    big = number[big[0]:big[1]]
    bignum = int(big)
    splitted = "[" + str(int(floor(bignum / 2))) + "," + str(int(ceil(bignum / 2))) + "]"
    return number.replace(big, splitted, 1)

def reduce(number):
    while is_nested(number) or is_big(number):
        nested = is_nested(number)
        while nested:
            number = explode(number, nested)
            nested = is_nested(number)
        big = is_big(number)
        if big:
            number = split(number, big)
    return number

def magnitude(sum):
    nested = re.search("\d+,\d+", sum)
    while nested:
        nested = nested.span()
        nums = [int(item) for item in sum[nested[0]:nested[1]].split(",")]
        sum = sum[:nested[0]-1] + str(nums[0] * 3 + nums[1] * 2) + sum[nested[1]+1:]
        nested = re.search("\d+,\d+", sum)
    return int(sum)

sum = data[0]
for item in data[1:]:
    sum = reduce(add(sum, item))

answer_a = magnitude(sum)
answer_b = max([magnitude(reduce(add(x, y))) for x in data for y in data if x != y])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b