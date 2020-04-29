"""
Mrs. Verma is continously working from last 15 hours and now she's getting tired .She asked her friend Miss Sharma to help her and her friend is ready to help .Now Mrs. Verma is explaining her friend how to calculate the grades.there are five subjects ,each student got some marks in particular subjects .On the basis of marks ,You've to calculate the percentage of each of the student and according to the percentage grade is assigned to the student and to assign the grades there are some conditions given below:

if (per>=90) then print grade is A .
if (per>=80 and per<90) then print grade is B.
if (per>=70 and per<80) then print grade is C.
if (per>=60 and per<70) then print grade is D.

otherwise print F.

Input Format

First line contains the marks of first subject,
second line contains the marks of second subject,
third line contains the marks of third subject,
Fourth line contains the marks of fourth subject
Fifth line contains the marks of fifth subject,
Constraints

0 <= marks <= 100

Output Format

Print the grade of the student. based on their percentage

Sample Input 0

90
90
90
90
90
Sample Output 0

A
Explanation 0

To calculate the percentage take the average of total marks and then according to the percentage print the grade.
"""

# Solution

sub = []

for i in range(5):
    sub.append(float(input()))

per = sum(sub)/5

if per >= 90:
    print("A")
elif per >= 80:
    print("B")
elif per >= 70:
    print("C")
elif per >= 60:
    print("D")
else:
    print("F")

