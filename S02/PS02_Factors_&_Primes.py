'''
Print all the factors of a given number
input : 12
output : 1 2 3 4 6 12
'''
'''
n = int(input("Enter a number: "))
for i in range (1, n+1):
    if n % i == 0:
        print(i,end=" ")
'''
'''
n = int(input("Enter a number: "))
for i in range (1,n//2+1):
    if n % i == 0:
        print(i,end=" ")
print(n)
'''
'''
Count the number of factors of a given number
input: 12
output : 6
'''
'''
n = int(input("Enter a number: "))
counter = 0
for i in range(1,n//2+1):
    if n % i == 0:
        counter += 1
print(counter+1)
'''
'''
Read a number from the user and check whether the given number is prime or not?
input : 7
output : prime

input : 9
output : not prime
 '''
'''n = int(input("Enter a number "))
counter = 0
for i in range(2,n//2+1):
    if n % i == 0:
        counter += 1
if counter == 0:
    print("Prime")
else:
    print("Not Prime")
'''
'''
Use ternary operator and reduce the number of lines in the code
'''
'''n = int(input("Enter a number "))
counter = 0
for i in range(2,n//2+1):
    if n % i == 0:
        counter += 1
print("Prime" if counter == 0 else "Not Prime")
'''
'''
print all the prime numbers in the given range
input : 1 10
output : 2 5 7
'''
'''
start = int(input())
end = int(input())
for n in range(start,end+1):
    counter = 0
    for i in range(2,n//2+1):
        if n % i == 0:
            counter += 1
    if counter == 0:
        print(n,end=" ")
'''
'''
Read a number from the user and display factorial of a number
input : 5
output : 120
'''
'''
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
'''
'''
Reverse Integer
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x = -1 * x
            rev = int(str(x)[::-1])
            return -1 * rev
        else:
            return int(str(x)[::-1])

        
