import sys

numbers = []
desired_sum = 2020

for i in sys.stdin:
    numbers.append(int(i))

for num1 in numbers:
    for num2 in numbers:
        if numbers.index(num2) is numbers.index(num1):
            continue

        if (num3 := desired_sum - (num1 + num2)) in numbers:
            print(
                f"The three numbers which add to get {desired_sum} are {num1}, {num2} and {num3}."
            )
            print(f"The product of these three numbers is {num1 * num2 * num3}.")
            exit()