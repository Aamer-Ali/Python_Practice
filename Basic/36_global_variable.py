a = 10
print(id(a))

def somthimg():
    # global a
    a = 9
    x = globals()['a']
    a = 15
    print(id(x))
    print("In Function ", x)
    globals()['a'] = 15


somthimg()
print("OutSide", a)
