import sys, requests
from bs4 import BeautifulSoup

def CheckForPTag(request):
    whereWeGo = requests.get('https://en.wikipedia.org/wiki/' + request)
    if whereWeGo.status_code != 200:
        print("It leads to a dead end !")
        sys.exit(0)
    soup = BeautifulSoup(whereWeGo.content, 'html.parser')
    soup = soup.find(id="mw-content-text")
    tagCheck = False
    tmp = None
    for link in soup.find_all('p'):
        if link.b:
            tagCheck = True
            tmp = link
            print(link.b.text)
            break
            
    if not tagCheck:
        print("It leads to a dead end !")
        sys.exit(0)
    aTags = tmp.find_all('a')
    if len(aTags) == 0:
        print("It leads to a dead end !")
        sys.exit(0)
    for a in aTags:
        if not a['href'].startswith('/wiki'):
            continue
        if a['href'].startswith('/wiki/Help'):
            continue
        theme = a['href'][6:]
        return (theme.replace("_", " "))

def loopOfRequests(request):
    roads = [request]
    while (request.lower() != 'philosophy'):
        request = CheckForPTag(request)
        if request is None:
            print("It leads to a dead end !")
            sys.exit(0)
        if request in roads:
            print('It leads to an infinite loop !')
            sys.exit(0)
        roads.append(request)
    return (roads)

def main():
    if len(sys.argv) != 2:
        print("Error : wrong number of arguments")
        sys.exit(0)
    numberOfRequests = loopOfRequests(sys.argv[1])
    if numberOfRequests[-1] == 'Philosophy':
        print(numberOfRequests[-1])
    print("{} roads from {} to philosophy".format(len(numberOfRequests), sys.argv[1]))

if __name__ == '__main__':
    main()