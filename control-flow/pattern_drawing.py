size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
 
# This script prints a square pattern of asterisks based on user input for size.
# The pattern will have 'size' number of rows and each row will contain 'size' number of asterisks.
# The outer loop iterates through each row, while the inner loop prints asterisks