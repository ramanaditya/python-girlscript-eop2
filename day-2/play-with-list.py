"""
Sherry and Payal are thinking about a problem which Lisha gave them. Lisha gave two numbers one to sherry and one to Payal, and asked to perform these operations

Create a List
Add a number given to Sherry in the List
Append the list with the number of Payal
Insert in between the average of both the number.
Insert at the beginning of the list the sum of the list
Insert at the end of the list the min of the list
Delete the number of sherry
Print the list

Input Format

First Line of input contains the number given to Sherry Second Line of input contains the number given to Payal

Constraints

\

Output Format

The Only Line contains th eList

Sample Input 0

5
6
Sample Output 0

[16.5, 5.5, 6, 5]
Explanation 0

Initially list = [5,6]
After inserting the avg in the middle = [5, 5.5, 6]
Adding sum at the beginning = [16.5, 5, 5.5, 6]
Adding minimum at the end = [16.5, 5, 5.5, 6, 5]
Deleting number of Sherry = [16.5, 5.5, 6, 5]
"""

# Solution

s = int(input())
p = int(input())

l = [s,p]
l.insert(1,(s+p)/2)
l.insert(0,sum(list))
l.append(min(list))
l.pop(1)

print(l)
