import sys, os, re, settings

def createHTMLFromTemplate(validFile):
    with open(validFile, "r") as file:
        data = file.read()
    data = data.format(name=settings.name, surname=settings.surname, age=settings.age, pro=settings.pro)
    print(data)
    with open('file.html', 'w') as f:
        f.write(data)

def FileCheck(filePath):
    try:
      open(filePath, "r")
      return 1
    except IOError:
      print ("Error: File does not appear to exist.")
      return 0

def render(template):
    if len(template) != 2:
        print ("Argument: No argument")
        sys.exit()
    filePath = template[1]
    if not FileCheck(filePath):
        sys.exit()
    if not filePath.endswith('.template'):
        print ("Argument needs extention: \".template\"")
        sys.exit()
    else:
        createHTMLFromTemplate(filePath)
        
    


if __name__ == '__main__':
    render(sys.argv)