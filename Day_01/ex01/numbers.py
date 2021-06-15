def numbers():
    with open('numbers.txt', 'r') as file:
        data = file.read().replace('\n', '')
    data = data.split(',')
    for i in data:
        print (i)
    file.close()

if __name__ == '__main__':
    numbers()