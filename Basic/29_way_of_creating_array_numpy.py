from numpy import *
#1) array()
arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

#2) linspace()
arr = linspace(0,15,16)  #braking the range into parts  0 to 15 in 16 parts
print(arr)


#3) arange()
arr = arange(1,15,2)  #start - end - step
print(arr)

#4) logspace()
arr = logspace(1,40,5)  #base on the log 10^1 to 10^40 divided into 5 parts
print(arr)

#5) Zeros()
arr = zeros(5,int)  #array of size 5 with value zero
print(arr)

#5) Onces()
arr = ones(5)  #array of size 5 with value one
print(arr)