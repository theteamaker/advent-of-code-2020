import sys

slope = (1, -3)
position = (0, 0)
multiplier = 1
trees = 0

for i in sys.stdin:
    for x in range(abs(slope[1]) - 1):
        sys.stdin.readline()

    i = i.strip("\n")
    string = i * multiplier

    if position[0] > (len(string) - 1):
        multiplier += 1
        string = i * multiplier

    if string[position[0]] == "#":
        trees += 1

    position = (position[0] + slope[0], position[1] + slope[1])

print(trees)
