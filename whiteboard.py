# Grasshopper - Summation
# DESCRIPTION:
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example (Input -> Output):
# summation(2) -> 3 (1 + 2)
# summation(8) -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


def whiteboard(num):
    if num == 1:
        return num
    else:
        return num + (whiteboard(num -1))

print(whiteboard(10))

)