'''
sample input : 1234
sample output : 4

sample input : 12236
sample output : 5
'''
'''
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)
'''
'''
sample input : 1234
sample output : 10

sample input : 12236
sample output : 14
Sum of digits in even numbers
'''
'''
n = int(input())
s = 0
while n > 0:
    s += (n % 10)
    n = n // 10
print(s)
'''
'''
sample input : 1234
sample output : 2 4

sample input : 12236
sample output : 2 2 6
print the even digits in one line
'''
'''
n = int(input())
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit, end=" ")
    n = n // 10
'''
'''
sample input : 1234
sample output : 4321
reverse the numbers
'''
def reverse(num):
    rev = 0
    while num > 0:
        rev = (rev*10) + (num % 10)
        num = num // 10
    return rev
'''
n = reverse(int(input()))
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10
'''
n = int(input())
temp = reverse(n)

print(temp == n)
if temp == n:
    print(True)
else:
    print(False)
print(True) if temp == n else print(False)




   




