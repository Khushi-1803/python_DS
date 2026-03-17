"""Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)."""
number = int(input("Enter a number: "))
if(number%2==0):
    print(f"{number} is even")
else:
    print(f"{number} is odd")