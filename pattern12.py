n = int(input("Enter number of rows: "))

for i in range(1, n + 1):  # Prints top part
    for j in range(i):  # Prints stars on left side
        print("*", end=" ")
    for j in range(2 * (n - i)):  # Prints spaces in the middle
        print(" ", end=" ")
    for j in range(i):  # Prints stars on right side
        print("*", end=" ")
    print()  #Moves to next line

for i in range(n - 1, 0, -1):  # Prints bottom part
    for j in range(i):  # Prints stars on left side
        print("*", end=" ")
    for j in range(2 * (n - i)):  # Prints spaces in the  middle
        print(" ", end=" ")
    for j in range(i):  # Prints stars on right side
        print("*", end=" ")
    print()  # Moves to next line