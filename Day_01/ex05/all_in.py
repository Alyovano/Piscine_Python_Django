import sys, re

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
        # print ("cap_key=", cap_key, "cap_value", cap_value)
        # print ("states_key", states_key,"states_value", states_value)
        if name == cap_value:
            isCapital(name, cap_key, states)
        elif name == states_key:
            isState(name, states_value, capital_cities)


def all_in(argv):
    if len(argv) != 2:
        return 1
    # parse_str = re.findall(r'\w+', argv[1])
    parse_str = argv[1].split(',')
    print ("VALUE=", parse_str)
    for i in parse_str:
        capitalOrCity(i)



    # tmp = ""
    # for key, value in capital_cities.items():
    #     if value == argv[1]:
    #         tmp = key
    #         break
    # if len(tmp) == 0:
    #     print ("Unknown state")
    # for key, value in states.items():
    #     if tmp == value:
    #         print(key)
    #         return 0
    



if __name__ == '__main__':
    all_in(sys.argv)
