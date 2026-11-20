n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):  # Runs from n to 1
    for j in range(n - i):  # Prints spaces before stars
        print("  ", end="")
    for j in range(2 * i - 1):  # Prints odd number of stars
        print("*", end=" ")
    print()  # Moves to next line