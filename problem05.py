# problem05:
# Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score
# You are given  scores. Store them in a list and find the score of the runner-up.
# The code starts here:

# Taking the array input
n = int (input())
A = list ()

# Appending the input values to the list 
for i in range(n):
 x = input ()
 A.append(x)  

# Sorting the input array to find out the second best and print out the second best
sortedlist = sorted(A)
print (sortedlist)
print (sortedlist [n-2])