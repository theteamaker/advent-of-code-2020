import sys

numbers = []
desired_sum = 2020

for i in sys.stdin:
    numbers.append(int(i))

for num1 in numbers:
    if (num2 := desired_sum - num1) in numbers:
        print(f"The two numbers which multiply to get {desired_sum} are {num1} and {num2}.")
        print(f"The product of these two numbers is {num1 * num2}.")
        break