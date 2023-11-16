def diamond(n):
    for i in range(n):    #responsible fpr creating the first half of the diamond 5
        for j in range(n - i - 1): # prints leading spaces 
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()   # Used to move to the next line after completing the row. Ensures the next row starts on a new line

# Example usage:
diamond(5)
