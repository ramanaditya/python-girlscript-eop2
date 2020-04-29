"""
Write a program to print the right triangled pattern upto n line.

Input Format

Only line of the input contains an interger n.

Constraints

1<= n <=26

Output Format

Output the required pattern upto n-lines.

Note:-Characters must be space sepreated.

Sample Input 0

5
Sample Output 0

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Explanation 0

Pattern upto 5 lines
"""

# Solution

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
      
    
