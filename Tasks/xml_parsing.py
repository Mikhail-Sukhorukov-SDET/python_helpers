from xml.etree.ElementTree import XMLParser


class RedGreenBlue:  # The target object of the parser
    depth = 0
    blue = 0
    red = 0
    green = 0

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1

        if attrib["color"] == "red":
            self.red += self.depth
        if attrib["color"] == "green":
            self.green += self.depth
        if attrib["color"] == "blue":
            self.blue += self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def close(self):  # Called when all data has been parsed.
        return self.red, self.green, self.blue


parser = XMLParser(target=RedGreenBlue())

parser.feed('<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>')
print(*parser.close())
