class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setNextNode(self, node):
        self.nextNode = node

    def getNextNode(self):
        return self.nextNode

    def getNodeValue(self):
        return self.value   

absheron = Node("01")
baku = Node("90")
bilesuvar = Node("12")

absheron.setNextNode(baku)
print(absheron.getNextNode().getNodeValue())

baku.setNextNode(bilesuvar)
print(baku.getNextNode().getNodeValue())

print(absheron.getNextNode().getNextNode().getNodeValue())