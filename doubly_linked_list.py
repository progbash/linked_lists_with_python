class dllNode(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None    

    def setNextNode(self, node):   
        self.nextNode = node

    def getNextNode(self):
        return self.nextNode
    
    def setPrevNode(self, node):
        self.prevNode = node

    def getPrevNode(self):
        return self.prevNode

    def getNodeValue(self):
        return self.value