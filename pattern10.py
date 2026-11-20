n = int(input("Enter number of rows: "))

for i in range(n):  # Runs the loop for  row
    for j in range(n):  # Runs the loop for  column
        if i == 0 or i == n-1 or j == 0 or j == n-1:# it checks the first and last rows,column
            print("*", end=" ")  # Prints stars on boundary
        else:
            print(" ", end=" ")  # Prints spaces inside
    print()  #Moves to next line