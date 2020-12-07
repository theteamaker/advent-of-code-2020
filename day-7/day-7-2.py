import sys

rules = {}
for i in sys.stdin:
    color, contains = i.split("contain")
    color = color.replace("bags", "")
    color = color.rstrip(" ")
    contains = [x.strip("\n") for x in contains.split(",")]
    contains = [x.replace("bags", "") for x in contains]
    contains = [x.replace("bag", "") for x in contains]
    contains = [x.rstrip(".") for x in contains]
    contains = [x.strip(" ") for x in contains]

    if "no other" in contains:
        continue

    to_append = []
    for x in contains:
        q = {}
        val = x[0]
        name = ""
        for y in range(0, 9):
            f = x.strip(str(y))
            if len(f) != len(x):
                name = f.strip(" ")
        
        q = {name: val}
        to_append.append(q)
    rules[color] = to_append

def lu(parent, value):
    sum = 0
    m = value 
    try:
        table = rules[parent]
    except:
        return value
    
    for child in table:
        for k, v in child.items():
            sum += lu(k, int(v)) * value
    
    return sum + value

print(lu(("shiny gold"), 1) - 1) # -1 because don't include the outside bag