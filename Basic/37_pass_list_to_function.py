def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd


lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]
even, odd = count(lst)
print("Total even are {} and odd are {}".format(even,odd))

#=======================Test=================================================================
#take 10 names from the user . count and display the names which have length more that letters

from numpy import  *

def countResult(lst):
    counter = 0
    for i in lst:
        if(len(i)>5):
            counter +=1
    return counter


namesList = []
n = int(input("Please enter the length of list : "))
for i in range(n):
    x = input("Enter Name : ")
    namesList.append(x)
result = countResult(namesList)
print("Total names having more than 5 charecters are {} ".format(result))