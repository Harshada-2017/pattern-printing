n =int(input("Enter a number:"))
for i in range(1,n+1): # this loop takes the number given by the user and starts from the 1
    # and the next number  
    for j in range(1,i+1): # prints number from 1 to i
            print(j,end="") # prints the number in the same line
    print()# moves to next line
    
    