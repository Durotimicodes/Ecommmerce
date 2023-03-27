
import random

"""
Fundamentals of Python

"""

if 5 > 3 :
    print("Five is greater than 3")
if 2 < 1 :
    print("One is less than two")

x = 5
y = "John"


x = str(3)
y = int(3)
z = float(5)

print(type(x),type(y),type(z))

A, B, C = 3, "Timi", 5
print(A,B,C)

fruits = ["apple", "grape", "banana"]
print(fruits[1])
print(A+C)


def myfunc():
    global x
    x = "fantastic"
    print("Python is "+ x)

myfunc()

print(x)

"""
DATA TYPES
you can not convert complex numbers into another number type
"""
X = ["apple", "banana", "cherry"] #LIST
y = {"apple", "banana", "strawberry"} #SET
D = frozenset({"apple", "easy pillers", "orange"}) #frozenset
T = ("girl", "boy", "infant") #tuple
Z = range(10) #range
r = {"name": "Oluwadurotimi", "Age": 29} #dict
U = bytearray(5) #bytearray
h = memoryview(bytes(5))

print("random Nos: ", random.randrange(1, 20))

for i in "Oluwadurotimi":
    print(len(i))
    break
#in 
#not in
txt = "the best things in life are free"
if "ee" not in txt:
    print("No", "not present")
else:
    print("present")
#format mehtod

age = 36
txt = "My name is Timi, and I am {}"
print(txt.format(age))