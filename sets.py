set1={"apple","mango","banana","orange","papaya"}
print(set1)
#for x in set1:
    #print(x)

#FUNCTIONS OF SETS
#add
set1.add("grapes")
print(set1)

#pop
b=set1.pop()
print(b)

#remove
set1.remove("grapes")
print(set1)

# Two example sets
setA = {1, 2, 3, 4}
setB = {3, 4}
setC = {10, 20}

print("SetA:", setA)
print("SetB:", setB)
print("SetC:", setC)

# 1. isdisjoint()
print("\nisdisjoint:")
print(setA.isdisjoint(setC))  # True (no common elements)
print(setA.isdisjoint(setB))  # False (3,4 are common)

# 2. issubset()
print("\nissubset:")
print(setB.issubset(setA))  # True (all elements of B are in A)

# 3. issuperset()
print("\nissuperset:")
print(setA.issuperset(setB))  # True (A contains all elements of B)

# 4. update()
print("\nupdate:")
setA.update(setC)  # adds elements of setC into setA
print("After update setA:", setA)

# 5. clear()
print("\nclear:")
setC.clear()  # removes all elements
print("After clear setC:", setC)

# Sample sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A =", A)
print("B =", B)

# -------------------------
# UNION
print("\nUnion:")
print("A | B =", A | B)

A_union = A.copy()
A_union.update(B)
print("A.update(B) =", A_union)

# -------------------------
# INTERSECTION
print("\nIntersection:")
print("A & B =", A & B)

A_inter = A.copy()
A_inter.intersection_update(B)
print("A.intersection_update(B) =", A_inter)

# -------------------------
# DIFFERENCE
print("\nDifference (A - B):")
print("A - B =", A - B)

A_diff = A.copy()
A_diff.difference_update(B)
print("A.difference_update(B) =", A_diff)

# -------------------------
# SYMMETRIC DIFFERENCE
print("\nSymmetric Difference:")
print("A ^ B =", A ^ B)

A_sym = A.copy()
A_sym.symmetric_difference_update(B)
print("A.symmetric_difference_update(B) =", A_sym)