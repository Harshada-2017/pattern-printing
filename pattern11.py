n = int(input("Enter number of rows: "))

for i in range(1, n + 1):  # Runs the loop for  row
    for j in range(1, i + 1):  # Prints stars in  row
        if j == 1 or j == i or i == n:#checks first and last positions and last row
            print("*", end=" ")  # Prints stars on boundary
        else:
            print(" ", end=" ")  # Prints spaces inside
    print()  # Moves to next line