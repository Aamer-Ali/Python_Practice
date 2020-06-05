# a + b ==>  int.__add__(a,b)
# Every thing in python is object
# Every operation is done in python by methods
# We can override the operator in our class
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # Addition
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):  # Greater Than
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False


s1 = Student(58, 69)
s2 = Student(90, 65)

s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print("S1 Wins")
else:
    print("S2 Wins")
