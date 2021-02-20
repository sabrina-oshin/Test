# problem06:
# The first line contains the integer n, the number of student's records
# The next  lines contain the names and marks obtained by a student, each value separated by a space
# The final line contains query_name, the name of a student to query
# Print the average of the marks array for the student name provided, showing 2 places after the decimal
# The code starts here:

# Defining the function 

def query_name ():
    if x is True:
        sum1 = A[1] + A[2] + A[3]
        avg1 = sum1/3
        print (avg1)
    elif y is True:
        sum2 = B[1] + B[2] + B[3]
        avg2 = sum2/3
        print (avg2)
    elif z is True:
        sum3 = C[1] + C[2] + C[3]
        avg3 = sum3/3
        print (avg3)
    else:
        return 0
    
# Taking the array input
n = int (input())

# Appending the user input in the list sequentially
A = list (map(int,input().strip().split())) [:n]
B = list (map(int,input().strip().split())) [:n]
C = list (map(int,input().strip().split())) [:n]

# Calling the defined function
query_name ()

