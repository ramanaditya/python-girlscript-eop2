"""
A teacher Liza wants to show the resultto their particular student's parents and every result is store in a unique page
of a file.For sometime teacher goe to drinks water and you've to help the teacher to showing the result. The unique
page consist of name of the student,roll no. of the student and percentage of the student.

Input Format

The first line of input contains a single integer T denoting the no. of testcases.Description of the T testcases follows:
The first line of T testcases contains a variable x representing the name of the student,second line contains a variable
n representing the roll no. of student and third line contains a variable k representing the marks of the student.

Constraints

1 <= |T| <= 100 1 <= |x| <= 20 1 <= |k| <= 100

Output Format

For each testcase, print the first unique line contains name of the student,second unique line contains roll no. of the student and third unique line contains marks of the student.

Sample Input 0

John
20
87.3
Sample Output 0

John
20
87.3
Sample Input 1

John
20
87.3
Sample Output 1

John
20
87.3
"""

# Solution

name = input()
roll_no = int(input())
marks = float(input())

print(name)
print(roll_no)
print(marks)