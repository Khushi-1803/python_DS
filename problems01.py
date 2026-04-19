#wap to find maximum out of three numbers
'''def max_num(val1,val2,val3):
    if(val1>=val2 and val1>=val3):
        print(f"{val1} is greater")
    elif(val2>=val1 and val2>=val3):
        print(f"{val2} is greater")
    else:
        print(f"{val3} is greater")
max_num(67,53,90)'''

#wap to print a list where the elements are the sqare from 1-30
'''list=[]
for i in range(1,31):
    list.append(i*i)
print(list)'''

#wap to check a number prime or not
'''num = int(input("Enter a number"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count=count+1
if(count==2):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")'''

#Fabbinocci series
def fabb(num):
    a=0
    b=1
    result = []
    for i in range(num):
        result.append(a)
        c=a+b
        a=b
        b=c
    return result
        
print(fabb(5))
       
