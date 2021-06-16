class Intern:
    def __init__ (self, 
                name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name
    
    def __str__ (self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

    class Coffee:
        def __init__ (self):
            self.worstCoffee = "This is the worst coffee you ever tasted."
        def __str__ (self):
            return self.worstCoffee


def internship():
    mark = Intern("Mark")
    noName = Intern()

    #Init two interns
    print("Intern name is:", mark.__str__())
    print("Intern name is:", noName.__str__())

    # Mark make coffee
    print(mark.make_coffee())

    # noName is trying to work
    try:
        noName.work()
    except Exception as error:
        print (error)


if __name__ == '__main__':
    internship()