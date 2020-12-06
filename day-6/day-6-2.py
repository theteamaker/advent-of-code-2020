import sys

lines = []
group = []
count = 0

for i in sys.stdin:
    lines.append(i)

for c, i in enumerate(lines):
    if i != "\n":
        group.append(i.strip("\n"))
        if (len(lines) - 1) != c:
            continue

    split_up = []
    for x in group:
        for y in x:
            split_up.append(y)

    uniques = set(x for l in split_up for x in l)

    for i in uniques:
        if split_up.count(i) == len(group):
            count += 1

    group = []
    continue

print(count)
