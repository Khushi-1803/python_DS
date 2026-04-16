Student_Data={"name":"John","age":24,"class":"X"}
# GETTING KEYS
for x in  Student_Data:
    print(x)
#GETTING VALUES
for x in Student_Data.values():
    print(x)
#GETTING KEYS AND VALUES
for x,y in Student_Data.items():
    print(x,":",y)

#FUNCTIONS OF DICTIONARY
#1️⃣get-> gives value of any key
a=Student_Data.get("name")
print(a)

#2️⃣item-> provide keys and value in tuple form
b=Student_Data.items()
print(b)


#3️⃣keys-> gives all keys
c=Student_Data.keys()
print(c)

#4️⃣keys-> gives all keys
d=Student_Data.values()
print(d)

#4️5️⃣keys-> gives all keys
e=Student_Data.copy()
print(e)

#NESTED DICTIONARY
employees = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

print(employees)
print(employees[1])
print(employees[1]["age"])

#PROBLEM SOLVING


#print dictionary where keys from 1-15 and values are there square
dict1={}
for x in range(1,16):
    dict1[x] = x*x
print(dict1)


#sorting keys of dictionay
dict2={3:9,1:1,2:2}
sorted_dict=dict(sorted(dict2.items()))
print(sorted_dict)

#sorting values of dictionay
dict3={3:9,1:1,2:2}
sorted_dict=dict(sorted(dict2.items(),key = lambda item: item[1]))
print(sorted_dict)

#sorting values of dictionay
dict3={3:9,1:1,2:2}
sorted_dict=dict(sorted(dict2.items(),key = lambda item: item[1],reverse=True))
print(sorted_dict)


