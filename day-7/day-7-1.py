import sys

fruit = {}
for i in sys.stdin:
    bag, allowed = i.split("contain")
    bag = bag.replace("bags", "")
    bag = bag.rstrip(" ")
    allowed = [x.strip("\n") for x in allowed.split(",")]
    allowed = [x.replace("bags", "") for x in allowed]
    allowed = [x.replace("bag", "") for x in allowed]
    allowed = [x.rstrip(".") for x in allowed]
    allowed = [x.strip(" ") for x in allowed]

    if "no other" in allowed:
        continue

    to_append = []
    for x in allowed:
        for y in range(0, 9):
            f = x.strip(str(y))
            if len(f) != len(x):
                z = f.strip(" ")
                to_append.append(z)
    
    fruit[bag] = to_append

bases = []

all_colors = []
for k, v in fruit.items():
    if k not in all_colors:
        all_colors.append(k)
    for i in v:
        if i not in all_colors:
            all_colors.append(i)

for k, v in fruit.items():
    if "shiny gold" in v:
        bases.append(k)

for i in bases:
    for k, v in fruit.items():
        if i in v and k not in bases:
            bases.append(k)

print(len(bases))