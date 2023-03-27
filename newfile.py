
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