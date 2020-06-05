from numpy import *

# arr1 = array([1,2,3,4,5])
# arr1 = arr1 + 5 #add 5 to each element
# print(arr1)


# arr2 = array([6,1,9,3,2])
# arr3 = arr1 + arr2
# print(arr3)

# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))


arr1 = array([1,2,3,4,5])
arr2 =arr1.view() #shallow copy
arr2 =arr1.copy() #deep copy
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))