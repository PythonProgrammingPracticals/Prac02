"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter an integer: "))
        finished = True
        pass
    except ValueError:
        print("That's not a valid answer. Try again.")

print("Nice! The valid result is:", result)
