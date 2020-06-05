# filter
# map
# reduce

# def is_even(n):
#      return  n%2 == 0
#
# nums =[3,2,5,4,3,6,8,9,4,2]
# evens = list(filter(is_even,nums))
# print(evens)

from functools import reduce

nums =[3,2,5,4,3,6,8,9,4,2]
evens = list(filter(lambda  n : n%2 == 0,nums))
doubles = list(map(lambda n : n+2,evens))
sums = reduce(lambda n,m : n+m ,doubles)
print(evens)
print(doubles)
print(sums)
