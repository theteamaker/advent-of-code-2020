import sys
from math import prod

lines = []
for i in sys.stdin:
    lines.append(i.strip("\n"))

slopes = [(1, -1), (3, -1), (5, -1), (7, -1), (1, -2)]


def encounters(lines, slope):
    position = (0, 0)
    multiplier = 1
    trees = 0

    count = abs(slope[1]) - 1

    for i in lines:
        if count != abs(slope[1]) - 1:
            count += 1
            continue

        string = i * multiplier

        if position[0] > (len(string) - 1):
            multiplier += 1
            string = i * multiplier

        if string[position[0]] == "#":
            trees += 1

        position = (position[0] + slope[0], position[1] + slope[1])

        count = 0

    return trees


results = []
for i in slopes:
    results.append(encounters(lines, i))

print(prod(results))