data =  [[tuple(map(int, beacon.split(","))) for beacon in scanner.split("\n")[1:]] for scanner in open("data/19.data").read().split("\n\n")]

import itertools

def solve():
    def transform(scanner, order, sign):
        transformed = []
        for beacon in scanner:
            transformed.append(tuple((beacon[order[i]] * sign[i] for i in range(len(beacon)))))
        return transformed

    def get_matches(x, y):
        max_matches = 0
        max_matches_diff = None
        for beacon_x in x:
            for beacon_y in y:
                diff = tuple(beacon_y[i] - beacon_x[i] for i in range(len(x[0])))
                matches = 0
                for other_beacon_y in y:
                    if tuple(other_beacon_y[i] - diff[i] for i in range(len(x[0]))) in x:
                        matches += 1
                if matches > max_matches:
                    max_matches = matches
                    max_matches_diff = diff
        return max_matches, max_matches_diff

    orders = list(itertools.permutations((0, 1, 2)))
    signs = list(itertools.product((1, -1), repeat=3))

    scanners = data.copy()
    scanners_aligned = [scanners[0]]
    added = [scanners[0]]
    checked = {i: False for i in range(len(scanners))}
    beacons = [beacon for beacon in scanners_aligned[0]]
    diffs = []
    while len(scanners_aligned) < len(scanners):
        for aligned in [scanner for scanner in scanners_aligned if not checked[scanners_aligned.index(scanner)]]:
            print(f" aligned:{len(scanners_aligned):>3}/{len(scanners):<3}[{','.join([str(scanners.index(scanner)) for scanner in added])}]")
            for scanner in scanners:
                if scanner not in added:
                    print(f"checking:{scanners.index(scanner):>3} vs {scanners.index(added[scanners_aligned.index(aligned)])}")
                    for order in orders:
                        for sign in signs:
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
            checked[scanners_aligned.index(aligned)] = True

    print(len(beacons))
    print(max([(sum([abs(x[i] - y[i]) for i in range(len(diffs[0]))])) for x in diffs for y in diffs if x != y]))


solve()