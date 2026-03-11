'''
#1) Creating a List
a=[10,20,30,40,50]
print(a)
b= list(10,20,312)
print(b)


#2) Accessing of List
a=[10,20,30,40,50]
print(a[0])
print(a[-1])


#3) Creating List with Repeated Elements
a=[10,20,30,40,50]
print(a * 2)


#4) Adding Elements to a List
a=[10,20,30,40,50]
a.append(100)
print(a)
a.insert(1,50)
print(a)


#5) Removing Elements from List
a=[10,20,30,40,50]
print(a)
a.pop()
print(a)


#6) Slicing
a=[10,20,30,40,50]
print(a[0:])
print(a[2:])


#2) Set Creation
a=set([10,20,30,450])
print(a)

#2) Adding
a=set([10,20,30,450])
a.add(80)
print(a)


#4) Removing --> Remove
a=set([10,20,30,450])
a.remove(50)
print(a)
'''

#5) Set Operation
a=set([10,20,30,450])
b=set([20,30,45,40])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
