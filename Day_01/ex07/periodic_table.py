def parseElem(elem):
    elem = elem.split(',')
    elem = [i.strip() for i in elem]
    elem = list(filter(None, elem))
    elem = [i for i in elem if i != []]
    return elem

def periodic():
    html = open("periodic_table.html", "a")
    html.write("<!DOCTYPE html>\n"
                "<html lang=\"en\">\n"
                "<head>\n"
                "   <meta charset=\"UTF-8\">\n"
                "   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
                "   <title>Document</title>\n"
                "</head>\n"
                "<body>\n"
                "    <table>\n")
    with open('periodic_table.txt', 'r') as file:
        data = file.read().split('\n')
    for elem in data:
        html.write("        <tr>\n")
        parsedElement = parseElem(elem)
        for i in parsedElement:
            html.write("            <td>")
            html.write(i)
            html.write("</td>\n")

        print (parsedElement)
        html.write("        </tr>\n")


    html.write("    </table>\n"
            "</body>\n"
            "</html>\n")

if __name__ == '__main__':
    periodic()