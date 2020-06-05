from abc import ABC, abstractclassmethod


class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running")


# com = Computer()
com1 = Laptop()
com1.process()
# com1.process()
