import sys

numbers = []
desired_sum = 2020

for i in sys.stdin:
    numbers.append(int(i))

for i1 in range(len(numbers)):
    num_index = i1

    for i2 in numbers:
        if numbers.index(i2) == num_index:
            continue

        if numbers[i1] + i2 == desired_sum:
            print(f"The two numbers which multiply to get {desired_sum} are {numbers[i1]} and {i2}.")
            print(f"The product of these two numbers is {numbers[i1] * i2}.")
            exit()