class HotBeverage:

    def description(self):
        return self.str_description

    def __str__(self):
        return "name: {name}\nprice: {price:,.2f}\ndescription: {description}".format \
            (name=self.name, price=self.price, description=self.description())

    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
        self.str_description = "Just some hot water in a cup"


class Coffee ( HotBeverage ):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"
        self.str_description = "A coffee, to stay awake."

class Tea ( HotBeverage ):
    def __init__(self):
        self.price = 0.30
        self.name = "tea"
        self.str_description = "Just some hot water in a cup."

class Chocolate ( HotBeverage ):
    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"
        self.str_description = "Chocolate, sweet chocolate..."

class Cappuccino ( HotBeverage ):
    def __init__(self):
        self.price = 0.45
        self.name = "cappuccino"
        self.str_description = "“Un po’ di Italia nella sua tazza!”"

def beverages():
    bev = HotBeverage()
    print(bev.__str__())

    cof = Coffee()
    print(cof.__str__())

    tea = Tea()
    print(tea.__str__())

    choco = Chocolate()
    print(choco.__str__())

    cappuc = Cappuccino()
    print(cappuc.__str__())



if __name__ == '__main__':
    beverages()