def add1(a,b):  #<- formal arguments
    c = a + b
    print(c)

add1(2,3)


def person(name,age):  #<- actual --  Position arguments
    print(name)
    print(age)

person('Aamer',30)



def person1(name,age):  #<- actual --  keyword arguments
    print(name)
    print(age)

person1(name='Aamer',age=30)


def person2(name,age = 28):  #<- actual --  default arguments
    print(name)
    print(age)

person2(name='Aamer')

def sum(a, *b):  #<- actual --  variable length arguments

    c = a
    for i in b:
        c = c + i
    print(c)

sum(5,6,43,78)

def sum1(*b):  #<- actual --  variable length arguments

    c = 0
    for i in b:
        c = c + i
    print(c)

sum1(5,6,43,78)