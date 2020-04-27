"""
Sherry and Lisha are best friends. But they keep on irritating each other. Lisha reverses everything Sherry speaks.
Lisha is a lazy girl, and she needs your help to automate this.

Write a code for Lisha which will automatically reverse the string given by Sherry.

You are given a string S and you have to print the reverse of this string S.

Input Format
String S

Constraints

1 <= |s| <= 100000

Output Format
Print the reverse of String S only. Don't print anything else.

Sample Input 0
Sherry

Sample Output 0
yrrehS

Sample Input 1
hello world

Sample Output 1
dlrow olleh
"""

# Solution

a = input()

print(a[::-1])