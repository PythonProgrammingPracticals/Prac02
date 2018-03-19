"""
CP1404/CP5632 - Practical
"""

#-------------- Exercise 01 -------------------
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# TODO: Using a for loop with the range function and string formatting,
# produce the following output:
#   0
#  50
# 100

#-------------- THINGS TO DO -------------------
print()
print()
numbers = [0, 50, 100,]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

print()
print()
#-------------- Random Numbers -------------------#
print("These are the random number answer to the example:")
import random
print(random.randint(5, 20))
#ans: is 5 is smallest.
#ans: is 20 largest.

print(random.randrange(3, 10, 2))
#ans: smallest number is 3
#ans: largest number is 9

print(random.uniform(2.5, 5.5))
#answer is 2.9434861140498296 // 2.5 for the smallest
#answer is 4.577902664963915 //  5.5 for the largest


print()
print()

