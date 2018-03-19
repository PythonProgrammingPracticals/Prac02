"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
#ans: occurs when the number is not an integer

2. When will a ZeroDivisionError occur?
#ans: You cannot divide 0 by 0. thus, 0 is undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#ans: yes it is possible. It is possible to attempt using "var_list" or "try..except".
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Error. The denominator must not be 0!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Done.")