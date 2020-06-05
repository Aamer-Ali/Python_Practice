# class A:
#     def __init__(self):
#         print('in A init')
#
#     def funtionOne(self):
#         print("Function One")
#
#     def functionTwo(self):
#         print("Function Two")
#
#
# class B(A):
#
#     def __init__(self):
#         super().__init__()
#         print("in B init")
#
#     def functionThree(self):
#         print("Function Three")
#
#     def functionFour(self):
#         print("Function Four")
#
# a = B()



# ================================= Method REsolution Order =========================
class A:
    def __init__(self):
        print('in A init')

    def funtionOne(self):
        print("Function One")

    def functionTwo(self):
        print("Function Two")


class B:
    def __init__(self):
        print("in B init")

    def functionThree(self):
        print("Function Three")

    def functionFour(self):
        print("Function Four")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")


a = C()
