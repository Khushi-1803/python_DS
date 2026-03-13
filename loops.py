#1️⃣WAP to find sum of all even numbers upto 50
sum = 0
for i in range(2,51,2):
    sum += i 
print(sum)    


#2️⃣WAP to firt 20 numbers and their squared number
for i in range(1,21):
    print(i,":",i*i)


#3️⃣Printing table of "n"
# n = int(input("Enter a number"))
# i=1
# while(i<11):
#     print(n, "x", i, "=", n*i)
#     i+=1


#4️⃣You are given a string s, you need to print its characters at even indices
s = "DoctorPhenomenal"
for char in range(0,len(s),2):
    print(s[char],end="")

#5️⃣ Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.    
x=10
while(x>0):
    print(x)
    x-=1

#6️⃣You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
a=int(input("Enter a number"))
if(a==0):print("already Zero")
else: 
    while(a>=0):
        print(a,end="")
        a-=1
