def flip_triangle(d):
    for i in range(d, 0, -1):   #prints rows
        for j in range(d - i):
            print(" ", end="")  #prints spaces
        for j in range(2 * i - 1):
            print("*", end="")  #prints *
        print()

flip_triangle(3)