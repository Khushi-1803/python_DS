# PRINTING OF SINGLE LINE
print("hello world")

# PRINTING OF MULTIPLE LINES

print("""Hello world!!
I hope you like it""")

print("Hello \nWorld!!")

print("it's going to rain")


# INPUT
# name = input("Enter your name...")
# age = int(input("Enter your age..."))
# side = float(input("Enter the side of triangle..."))
# print(name)
# print(age)
# print(side)

#EXPLICIT AND IMPLICIT CONVERSION
a=12
b=14.8
c=a+b
print(c)

a="12"
a=int(a)
b=14.8
c=a+b
print(c)

a=5678
b="5678"
print(a is b)
print(a is not b)

#Given two inputs that are stored in variables a and n, you need to print a, n times in a single line without space between them. Output must have a newline at the end.
a = "Hello"
n = 5
print(a*n)

#Given three inputs that are stored in the variables a, b, and c. You need to print a a times and b b times  in a single line separated by c.
a = int(input("Enter a number"))
b = int(input("Enter second number"))
c = input()

result = (str(a) * a) + c + (str(b) * b)
print(result)
