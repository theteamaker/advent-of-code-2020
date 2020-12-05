import sys, math

highest_seat = 0

for i in sys.stdin:
    letters = [x for x in i.strip("\n")]

    lowest = 0
    highest = 127

    row = 0
    column = 0

    def bounds(bounds, characters):
        lowest, highest = bounds

        if characters[0] == "F" or characters[0] == "L":
            highest = math.floor((highest / 2) + (lowest / 2))
        elif characters[0] == "B" or characters[0] == "R":
            lowest = math.ceil((highest / 2) + (lowest / 2))

        return(lowest, highest)
    
    while len(letters) != 3:
        lowest, highest = bounds((lowest, highest), letters)
        letters.remove(letters[0])
        row = lowest
        continue

    lowest = 0
    highest = 7

    while len(letters) != 0:
        lowest, highest = bounds((lowest, highest), letters)
        letters.remove(letters[0])
        column = lowest
    
    seat_id = (row * 8) + column

    if seat_id > highest_seat:
        highest_seat = seat_id

print(highest_seat)