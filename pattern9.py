n = int(input("Enter number of rows: "))

for i in range(1, n + 1):  # Prints the top part
    for j in range(n - i):  # Prints spaces
        print("  ", end="")
    for j in range(2 * i - 1):  # Prints stars
        print("*", end=" ")
    print()  # Moves to next line

for i in range(n - 1, 0, -1):  # Prints bottom part
    for j in range(n - i):  # Prints spaces
        print("  ", end="")
    for j in range(2 * i - 1):  # Prints stars
        print("*", end=" ")
    print()  # Moves to next line