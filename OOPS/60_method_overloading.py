# Method overloading is not supported as tradition eg.JAVA
# We have to use different approach as follows

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(58, 69)

print(s1.sum(1, ))
print(s1.sum(1, 2))
print(s1.sum(1, 2, 3))
