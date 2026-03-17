""" Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

 Return True for the following cases:

 Either a or b (not both) is non-negative and the flag is false.
 Both a and b are negative and the flag is true."""

a = int(input("Enter a number"))
b = int(input("Enter the second  number"))
flag = input("Enter the boolean value")
if (((a >= 0 and b < 0) or (a < 0 and b >= 0)) and flag == "false"):
    print("True")
elif(a<0 and b<0 and flag=="true"):
    print("True")
else:
    print("False")