#Q1
a=[1,2,3,4]
a.reverse()
print(a)

#Q2
Str="Welcome To World Of Python"
upper=""
for letter in Str:
    if letter.isupper():
        upper=upper+letter+','
print("All uppercase letters:",upper)

#Q3
a=input("enter value:")
c=a.split(',')
b=[]
for i in c:
    b.append(int(i))
print(b)

#Q4
Str="madam"
rev=Str[::-1]
if Str==rev:
    print('String is a palindrome')
else:
    print('String is not a palindrome')

#Q5
import copy as c
list1=[1,2,3,[4,6],5]
list2=c.deepcopy(list1)
list1[3][1]='hello'
list1[2]='wow'
print(list1)
print(list2)

Shallow Copy: A shallow copy creates a new object which stores the reference of the original elements.
So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

Deep Copy: A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
However, we are going to create deep copy using deepcopy() function present in copy module. The deep copy creates independent copy of original object and all its nested objects.

    
