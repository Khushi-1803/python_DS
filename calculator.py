"""Given two numbers a and b; you need to perform basic mathematical operation on them. You will be provided an integer named as operator. 
If operator equals to 1 add a and b, then print the result as a string.
If operator equals to 2 subtract b from a, then print the result as a string.
If operator equals to 3 multiply a and b, then print the result as a string.
If operator equals to any another number, print "Invalid Input"(without quotes)."""

def utility(a, b, opr):
    if(opr==1):
        print(f"{a}+{b} = {a+b}")
    elif(opr==2):
        print(f"{a}-{b} = {a-b}")
    elif(opr==3):
        print(f"{a}x{b} = {a*b}")
    elif(opr==4):
        print(f"{a}/{b} = {a/b}")
    else:
        print("Invalid input")
utility(9,1,4)