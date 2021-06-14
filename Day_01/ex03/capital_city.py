import sys

def capital(argv):
    if len(argv) != 2:
        print ("Need one argument")
        return 1
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    tmp = ""
    for key, value in states.items():
        if key == argv[1]:
            tmp = value
            break
    if len(tmp) == 0:
        print ("Unknown state")
    for key, value in capital_cities.items():
        if tmp == key:
            print(value)
            return 0
    



if __name__ == '__main__':
    capital(sys.argv)
