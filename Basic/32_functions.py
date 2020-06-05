def greet():
    print('Hello')

def add(x,y):
    return x+y

def add_sub(x,y):
    c = x + y
    d= x - y
    return  c,d

greet()
print(add(2,3))

result1,result2 = add_sub(5,3)
print(result1,result2)