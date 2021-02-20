# problem05:
# Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score
# You are given  scores. Store them in a list and find the score of the runner-up.
# The code starts here:

# Taking the array input
n = int (input())

# Appending the user input in the list sequentially
A = list (map(int,input().strip().split())) [:n]

# Code to find out the second highest number in a list
mx =max(A[0],A[1]) 
secondmax =min(A[0],A[1]) 
for i in range(2,n): 
    if A[i]>mx: 
        secondmax=mx
        mx=A[i] 
    elif A[i]>secondmax and \
        mx != A[i]: 
        secondmax=A[i]

# Print the second highest number in a list
print(str(secondmax))
