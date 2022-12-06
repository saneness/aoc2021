from aocd.models import Puzzle
from numpy import prod

puzzle = Puzzle(year=2021, day=22)
data = [item.split() for item in puzzle.input_data.split("\n")]
data = [[item[0], [tuple(map(int, subitem.split("=")[-1].split(".."))) for subitem in item[1].split(",")]] for item in data]

def intersect(cube1, cube2):
    for i in range(3):
        if cube1[i][0] > cube2[i][1] or cube1[i][1] < cube2[i][0]:
            return None
    return [tuple((max(cube1[i][0], cube2[i][0]), min(cube1[i][1], cube2[i][1]))) for i in range(3)]

def split(cube1, cube2):
    intersection = intersect(cube1, cube2)
    if not intersection:
        return [cube1]
    splitted = []
    splitted.append([cube1[0], cube1[1], (cube1[2][0], intersection[2][0] - 1)])
    splitted.append([cube1[0], cube1[1], (intersection[2][1] + 1, cube1[2][1])])
    splitted.append([intersection[0], (cube1[1][0], intersection[1][0] - 1), intersection[2]])
    splitted.append([intersection[0], (intersection[1][1] + 1, cube1[1][1]), intersection[2]])
    splitted.append([(cube1[0][0], intersection[0][0] - 1), cube1[1], intersection[2]])
    splitted.append([(intersection[0][1] + 1, cube1[0][1]), cube1[1], intersection[2]])
    return [cube for cube in splitted if cube[0][0] <= cube[0][1] and cube[1][0] <= cube[1][1] and cube[2][0] <= cube[2][1]]

states = [item[0] == "on" for item in data]
cubes = [item[1] for item in data]

def reboot(init=False):
    cubes_on = []
    for state, cube in zip(states, cubes):
        if init:
            cube = intersect(cube, [(-50, 51), (-50, 51), (-50, 51)])
        if cube:
            cubes_splitted = []
            for cube_on in cubes_on:
                for cube_splitted in split(cube_on, cube):
                    cubes_splitted.append(cube_splitted)
            if state:
                cubes_splitted.append(cube)
            cubes_on = cubes_splitted
    return sum([prod([cube[i][1] + 1 - cube[i][0] for i in range(3)]) for cube in cubes_on])

answer_a = reboot(init=True)
answer_b = reboot()

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b