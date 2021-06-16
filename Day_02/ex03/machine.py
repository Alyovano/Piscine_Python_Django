from beverages import HotBeverage, Coffee, Chocolate, Tea, Cappuccino
import random

class CoffeeMachine:
    used = 0
    def __init__(self):
        pass

    class EmptyCup ( HotBeverage ):
        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"
            self.str_description = "An empty cup?! Gimme my money back!"

    class BrokenMachineException( Exception ):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.used = 0

    def serve(self, drink):
        if self.used > 9:
            raise self.BrokenMachineException()
        self.used += 1
        if random.randint(0, 1) == 0:
            return drink()
        else:
            return self.EmptyCup()


def machine():
    senseo = CoffeeMachine()

    for i in range(10):
        try:
            cup = senseo.serve(Coffee)
            print(cup.__str__())
            print(senseo.used)
        except Exception as error:
            print(error)
    senseo.repair()
    for i in range(10):
        try:
            cup = senseo.serve(Coffee)
            print(cup.__str__())
            print(senseo.used)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    machine()