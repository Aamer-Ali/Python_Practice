class Computer:
    def __init__(self):
        self.name = "Aamer"
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
# c1.age = 23  #comment and uncomment to change the result
c2 = Computer()

if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")
