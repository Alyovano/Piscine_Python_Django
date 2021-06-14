import sys

def state(argv):
    if len(argv) != 2:
        print ("Need one argument")
        return 1

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }


    tmp = ""
    for key, value in capital_cities.items():
        if value == argv[1]:
            tmp = key
            break
    if len(tmp) == 0:
        print ("Unknown capital city")
    for key, value in states.items():
        if tmp == value:
            print(key)
            return 0
    



if __name__ == '__main__':
    state(sys.argv)
