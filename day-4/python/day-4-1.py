import sys

lines = []
case = []
case_dict = {}
valid = 0

for i in sys.stdin:
    lines.append(i)

for c, i in enumerate(lines):
    if i != "\n":
        [
            case.append(x)
            for x in [y.split(":") for y in [x.strip("\n") for x in i.split(" ")]]
        ]
        if (len(lines) - 1) != c:
            continue

    case_dict = {k: v for k, v in (case)}

    if len(case_dict) == 7 and "cid" not in case_dict.keys():
        valid += 1
    elif len(case_dict) == 8:
        valid += 1

    case.clear()
    case_dict.clear()

print(valid)
