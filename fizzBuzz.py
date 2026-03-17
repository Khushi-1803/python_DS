"""You are given a number  and you have to print your answer according to the following:
If the number is divisible by 3, you print "Fizz" (without quotes)
If the number is divisible by 5, you print "Buzz" (without quotes)
If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
In any other case, you print the number itself"""

def fizzBuzz(num):
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif(num%5==0):
        print("Buzz")
    elif(num%3==0):
        print("Fizz")
    else:
        print(num)
fizzBuzz(1)