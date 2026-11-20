
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):  # Runs from 1 to n
    for j in range(n - i):  # Prints Spaces before the stars
        print("  ", end="")
    for j in range(2 * i - 1):  # Prints odd number of stars
        print("*", end=" ")
    print()  # Moves to next line