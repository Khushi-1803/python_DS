#You have to take an interger input a, and then use the if statement to print "Big" (without quotes) if the given number is greater than 100, and use the else statement to print "Small" (without quotes) when the number is smaller than or equal to 100.

a = int(input("Enter a number"))
if a > 100 : print("Big")
else: print("Small") 

#1️⃣ Write a program to check whether a number is even or odd.
b = int(input("Enter a number"))
if(b%2==0) : print(f"{b} is even")
else: print(f"{b} is odd")

#2️⃣ Write a program to check whether a number is positive, negative, or zero.
c= int(input("Enter a number"))
if(c>0):print(f"{c} is positive number")
elif(c<0):print(f"{c} is negative number")
else:print(f"{c} is zero")

#3️⃣ Write a program to find the largest of three numbers.
d  =int(input("Enter a number"))
e  =int(input("Enter the second number"))
f  =int(input("Enter the third number"))
if(d>=e and d>=f):print(f"{d} is greater than {e} and {f}")
elif(e>=d and e>=f):print(f"{e} is greater than {d} and {f}")
else:print(f"{f} is greater than {d} and {e}")

#4️⃣ Write a program to check whether a number is divisible by both 5 and 11.
g = int(input("Enter a number"))
if(g%5==0 and g%11==0):print(f"{g} is divisible from both 5 and 11")
else:print(f"{g} is not divisible from both 5 and 11")

#5️⃣ Write a program that takes a number and prints "Positive Even", "Positive Odd", "Negative Even", or "Negative Odd".

h = int(input("Enter a number"))

if h > 0 and h % 2 == 0:
    print("Positive Even")
elif h > 0 and h % 2 != 0:
    print("Positive Odd")
elif h < 0 and h % 2 == 0:
    print("Negative Even")
elif h < 0 and h % 2 != 0:
    print("Negative Odd")
else:
    print("Zero")