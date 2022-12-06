from aocd.models import Puzzle
from itertools import permutations, product

puzzle = Puzzle(year=2021, day=19)
data =  [[tuple(map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]] for scanner in puzzle.input_data.split("\n\n")]

def transform(scanner, order, sign):
    transformed = []
    for beacon in scanner:
        transformed.append(tuple((beacon[order[i]] * sign[i] for i in range(len(beacon)))))
    return transformed

def get_matches(x, y):
    max_matches = 0
    max_matches_diff = None
    matched = False
    for beacon_x in x:
        if not matched:
            for beacon_y in y:
                if not matched:
                    diff = tuple(beacon_y[i] - beacon_x[i] for i in range(len(x[0])))
                    matches = 0
                    for other_beacon_y in y:
                        other_diff = tuple(other_beacon_y[i] - diff[i] for i in range(len(x[0])))
                        if other_diff in x:
                            matches += 1
                    if matches > max_matches:
                        max_matches = matches
                        max_matches_diff = diff
                        if matches >= 12:
                            matched = True

    return max_matches, max_matches_diff

orders = list(permutations((0, 1, 2)))
signs = list(product((1, -1), repeat=3))
even_orders = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
even_signs = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
odd_orders = [(0, 2, 1), (1, 0, 2), (2, 1, 0)]
odd_signs = [(1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1)]

scanners = data.copy()
scanners_aligned = [scanners[0]]
added = [scanners[0]]
checked = {i: False for i in range(len(scanners))}
beacons = [beacon for beacon in scanners_aligned[0]]
diffs = []
while len(scanners_aligned) < len(scanners):
    for aligned in [scanner for scanner in scanners_aligned if not checked[scanners_aligned.index(scanner)]]:
        for scanner in scanners:
            if scanner not in added:
                matched = False
                for order in orders:
                    for sign in signs:
                        if order in even_orders and sign in even_signs or order in odd_orders and sign in odd_signs:
                            if not matched:
                                transformed = transform(scanner, order, sign)
                                matches, diff = get_matches(aligned, transformed)
                                if matches >= 12:
                                    scanner_aligned = [tuple(beacon[i] - diff[i] for i in range(len(diff))) for beacon in transformed]
                                    scanners_aligned.append(scanner_aligned)
                                    diffs.append(diff)
                                    for beacon in scanner_aligned:
                                        if beacon not in beacons:
                                            beacons.append(beacon)
                                    added.append(scanner)
                                    matched = True
        checked[scanners_aligned.index(aligned)] = True

answer_a = len(beacons)
answer_b = max([(sum([abs(x[i] - y[i]) for i in range(len(diffs[0]))])) for x in diffs for y in diffs if x != y])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b