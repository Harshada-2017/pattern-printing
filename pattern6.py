
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):  # prints according user input
    for j in range(n - i):  # spaces decreses as the number of row incerses
        print("  ", end="")  # Gives space
    for j in range(i):  # Runs according to row number
        print("*", end=" ")  # Print stars
    print()  # Moves to next line