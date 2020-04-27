"""
Akshay is a teacher and he is calculating the end sum result of the students of his class. He is bored of calculating
 the result by his own. He wants you to calculate the total marks and percentage of each student.

You will be given marks of python, cpp and java. You have to find the total marks and percentage and print in the
separate lines.

Input Format

First Line of Input contains marks of python Second Line of Input contains marks of cpp Three Line of Input contains
marks of java

Constraints

All marks will be between 0 <= marks <= 100

Output Format

First Line of Output contains Total Marks ie., sum of marks of python, cpp and java Second Line of Output contains
percentage of the students.

Sample Input 0
50
90
80

Sample Output 0
220
73.33333333333333

Sample Input 1
96
93
73

Sample Output 1
262
87.33333333333333
"""

# Solution

marks1 = int(input())
marks2 = int(input())
marks3 = int(input())

total_marks = marks1+marks2+marks3

percentage = (total_marks/300)*100

print(total_marks)
print(percentage)