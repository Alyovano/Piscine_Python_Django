import antigravity 
import sys


def geoh(arg):
    try:
        antigravity.geohash(float(arg[1]), float(arg[2]), bytes(arg[3], 'UTF-8'))
    except Exception as error:
        print(error)

if __name__ == '__main__':
    geoh(sys.argv)