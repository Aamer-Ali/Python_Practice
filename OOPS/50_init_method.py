class Computer:
    def __init__(self, cpu, ram):  # Its like a constructor
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("CPU = {} and RAM = {}".format(self.cpu, self.ram))


com1 = Computer('i5', 8)
com2 = Computer('Ryzen', 16)
com1.config()
com2.config()
