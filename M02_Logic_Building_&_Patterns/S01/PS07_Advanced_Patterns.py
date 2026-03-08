'''
1. Pascl Triangle
n = 5
Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
'''
n = int(input())
for i in range(1,n+1):
    num = 1
    for j in range(i):
        print(num,end=" ")
        num = num * (i-j)//(j+1)
    print()
'''
'''
2. Butterfly Pattern
n = 4
Output:
*       *
**     **
***   ***
*********
*********
***   ***
**     **
*       *
'''
n = int(input())
for i in range(1,n+1):
    print("*" * i + " " * (2 * (n-i)) + "*" * i)
for j in range(n, 0, -1):
    print("*" * j + " " * (2 * (n-j)) + "*" * j)
     
