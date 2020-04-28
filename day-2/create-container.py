"""
A professor asked Lisha to list up all the marks in front of her name but she doesn't know how to do it.

Help her to use a container that solves this problem.

Input Format

First line of input contains name Next three lines contains marks of a student in three subjects.

Constraints

type(marks) = int

Output Format

Print the container which contains the name and all the marks and can be accessed easily

NOTE: Use the variable name to store name and varibale marks to store the marks

Sample Input 0

Lisha
98
97
99
Sample Output 0

{'name': 'Lisha', 'marks': [98, 97, 99]}
"""

# Solution
name=input()
marks=[]
marks.append(int(input()))
marks.append(int(input()))
marks.append(int(input()))

d={}
d["name"]=name
d["marks"]=marks

print(d)
