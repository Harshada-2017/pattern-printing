n =int(input("Enter a number:"))
for i in range(1,n+1): # this loop takes the number given by the user and starts from the 1
    # and the next number  
    for j in range(i): # runs as per the number of row
            print(i,end="") # prints the same number in the row
    print() # moves to the next line