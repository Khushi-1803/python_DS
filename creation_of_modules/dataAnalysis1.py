import numpy as np;

arr = np.array([10,20,30,40])

arr2 = np.array([[10,20,30,40],[50,60,70,80],[56,89,80,79]])

# print(arr)
# print(arr[0:3])

# print(arr2)
# print(arr2[0:2,0:2])
# print(arr2[0,0:3])
# print(arr2[1,1:3])

# Attributes of array
print(np.shape(arr2))
print(np.size(arr2))
print(np.ndim(arr2))  #dimension-2d
print(arr2.dtype)
print(len(arr2))

print(type(arr))