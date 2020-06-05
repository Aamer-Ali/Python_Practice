class A:
    def funtionOne(self):
        print("Function One")

    def functionTwo(self):
        print("Function Two")


class B(A):
    def functionThree(self):
        print("Function Three")

    def functionFour(self):
        print("Function Four")


class C(B):
    def functionFive(self):
        print("Function Five")


objC = C()
objC.funtionOne()
