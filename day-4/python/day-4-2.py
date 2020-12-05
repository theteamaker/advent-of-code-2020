import sys
import re

lines = []
case = []
case_dict = {}
valid = 0

for i in sys.stdin:
    lines.append(i)


def validator(dictionary):
    def basic_check():
        return (
            len(dictionary) == 7
            and "cid" not in dictionary.keys()
            or len(dictionary) == 8
        )

    def year_check(value, least, most):
        return len(value) == 4 and int(value) >= least and int(value) <= most

    def hgt_check(value):
        def re_concat(result):
            string = ""
            for i in result:
                string += i
            return string

        unit = re_concat(re.findall(r"\D", value))
        measure = re_concat(re.findall(r"\d", value))

        if unit != "in" and unit != "cm":
            return False
        try:
            int(measure)
        except:
            return False

        if unit == "in":
            return int(measure) >= 59 and int(measure) <= 76
        if unit == "cm":
            return int(measure) >= 150 and int(measure) <= 193

    def hcl_check(value):
        return len(re.findall(r"(#{1}[0-f]+)", value)) == 1

    def ecl_check(value):
        valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        for i in valid:
            if value == i:
                return True

        return False

    def pid_check(value):
        try:
            int(value)
        except:
            return False

        return len(value) == 9

    if basic_check() is False:
        return False

    fruit = [
        year_check(dictionary["byr"], 1920, 2002),
        year_check(dictionary["iyr"], 2010, 2020),
        year_check(dictionary["eyr"], 2020, 2030),
        hgt_check(dictionary["hgt"]),
        hcl_check(dictionary["hcl"]),
        ecl_check(dictionary["ecl"]),
        pid_check(dictionary["pid"]),
    ]

    for i in fruit:
        if i is False:
            return False

    return True


for c, i in enumerate(lines):
    if i != "\n":
        [
            case.append(x)
            for x in [y.split(":") for y in [x.strip("\n") for x in i.split(" ")]]
        ]
        if (len(lines) - 1) != c:
            continue

    case_dict = {k: v for k, v in (case)}

    if validator(case_dict) is True:
        valid += 1

    case.clear()
    case_dict.clear()

print(valid)
