import sys

def isCapital(name, check, states):
    for key, value in states.items():
        if check == value:
            print (name, "is the capital of", key)
            break

def isState(name, check, capital_cities):
    for key, value in capital_cities.items():
        if check == key:
            print (name, "is the state of", value)
            break


def capitalOrCity(name):
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
    for (cap_key, cap_value), (states_key, states_value) in zip(capital_cities.items(), states.items()):
        if name == cap_value:
            isCapital(name, cap_key, states)
            return 0
        elif name == states_key:
            isState(name, states_value, capital_cities)
            return 0
    print (name, "is neither a capital city nor a state")


def all_in(argv):
    if len(argv) != 2:
        return 1
    parse_str = argv[1].split(',')
    parse_str = [i.lower() for i in parse_str]
    parse_str = [i.title() for i in parse_str]
    for i in range(len(parse_str)):
        parse_str[i] = parse_str[i].strip()
    for i in parse_str:
        if not i:
            pass
        else:
            capitalOrCity(i)



if __name__ == '__main__':
    all_in(sys.argv)
