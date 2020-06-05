from numpy import *
#
# arr1 = array([
#     [1, 2, 3, 6, 2, 9],
#     [4, 5, 6, 7, 5, 3]
# ])
#
# arr2 = arr1.flatten()
# print(arr2)
#
# arr3 = arr2.reshape(2,2,3)
# print(arr3)
#
#
#
# # print(arr1)
# # print(arr1.dtype)
# # print(arr1.ndim)
# # print(arr1.shape)


# arr1 = array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
#
# m  = matrix(arr1)
# print(m)
#
#


# m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
# print(m)
# print()
# print(diagonal(m))
# print()
# print(m.max())


m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')

m3 = m1 * m2
print(m3)